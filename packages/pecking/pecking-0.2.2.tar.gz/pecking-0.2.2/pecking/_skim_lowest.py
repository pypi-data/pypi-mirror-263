import itertools as it
import statistics
import typing
import warnings

import numpy as np
from scipy import stats as scipy_stats


def _do_skim_lowest(
    samples: typing.Sequence[typing.Sequence[float]],
    labels: typing.Optional[typing.Sequence[typing.Union[str, int]]] = None,
    *,
    alpha: float = 0.05,
    min_obs: int = 0,
    nan_policy: typing.Literal["propagate", "raise", "omit"] = "raise",
    reverse: bool = False,
) -> typing.List[typing.Union[str, int]]:
    """Implementation detail for skim_lowest."""
    if labels is None:
        labels = [*range(len(samples))]

    # Remove samples with fewer than `min_obs` observations.
    samples_, labels_ = zip(
        *(
            (sample, label)
            for sample, label in zip(samples, labels)
            if len(sample) >= min_obs
        ),
    )

    if len(samples_) < len(samples):
        warnings.warn(
            f"Skipped {len(samples) - len(samples_)} samples with fewer than "
            f"{min_obs} observations.",
        )
    samples, labels = samples_, labels_

    if len(samples) < 2:
        raise ValueError("At least two samples are required.")

    h, p_kruskal = scipy_stats.kruskal(*samples, nan_policy=nan_policy)
    assert 0 <= p_kruskal <= 1 or np.isnan(p_kruskal)
    if np.isnan(p_kruskal) and nan_policy == "raise":
        raise ValueError("Kruskal-Wallis H test returned NaN p-value.")
    if p_kruskal > alpha or np.isnan(p_kruskal):
        return []

    population = sorted([*it.chain(*samples)], reverse=reverse)

    def get_rank(value: float) -> float:
        return np.mean(
            [
                np.searchsorted(population, value, side="left"),
                np.searchsorted(population, value, side="right"),
            ],
        )

    rank_means = [statistics.mean(map(get_rank, sample)) for sample in samples]
    slice_ = slice(None, None, -1) if reverse else slice(None, None)
    rank_mean_order = np.argsort(rank_means)[slice_]

    skimmed = []
    for i, position in enumerate(rank_mean_order):
        if i == 0:
            skimmed.append(labels[position])
            continue

        alpha_ = alpha / i
        u, p = scipy_stats.mannwhitneyu(
            samples[position],
            samples[rank_mean_order[0]],
            alternative="less" if reverse else "greater",
            nan_policy=nan_policy,
        )
        assert 0 <= p <= 1 or np.isnan(p), p
        if np.isnan(p) and nan_policy == "raise":
            raise ValueError("Mann-Whitney U test returned NaN p-value.")
        if p > alpha_:
            skimmed.append(labels[position])
        elif np.isnan(p):
            continue
        else:
            break

    if len(skimmed) == len(labels):
        warnings.warn(
            "Lowest ranked group and highest ranked group are "
            "indistinguishable by Mann-Whitney U test, in contradiction to "
            f"Kruskal-Wallis test result p={p_kruskal}.",
        )
        return []
    else:
        return skimmed


def skim_lowest(
    samples: typing.Sequence[typing.Sequence[float]],
    labels: typing.Optional[typing.Sequence[typing.Union[str, int]]] = None,
    *,
    alpha: float = 0.05,
    min_obs: int = 0,
    nan_policy: typing.Literal["propagate", "raise", "omit"] = "raise",
    reverse: bool = False,
) -> typing.List[typing.Union[str, int]]:
    """Identify the set of lowest-ranked groups that are statistically
    indistinguishable amongst themselves based on a Kruskal-Wallis H-test
    followed by multiple Mann-Whitney U-tests.

    Parameters
    ----------
    samples : Sequence[Sequence[float]]
        A sequence of sequences, where each inner sequence represents a sample
        group with numerical data.
    labels : Optional[Sequence[Union[str, int]]], optional
        A sequence of labels corresponding to each sample group.

        If not provided, numeric labels starting from 0 are assigned.
    alpha : float, default 0.05
        Significance level for the statistical tests.

        Used to determine if the difference between groups is significant.
    min_obs : int, default 0
        The minimum number of observations required for a sample to be included
        in the analysis.

        Samples with fewer observations than `min_obs` will be omitted from
        skimming. Useful especially if the lowest ranked group has very few
        observations so cannot be meaningfully compared to the others.
    nan_policy : {'propagate', 'raise', 'omit'}, default 'raise'
        Defines how to handle NaNs in the input data.

            'propagate': If a NaN is present in the data, the corresponding
            output will be NaN.

            'omit': NaNs will be omitted from the calculations. If insufficient
            data remains after omitting NaNs, the corresponding output will be
            NaN.

            'raise': If a NaN is detected in the input data, a ValueError will
            be raised.
    reverse : bool, default False
        If True, skims the highest ranked samples instead of the lowest.

        Prefer `pecking.skim_highest` for better readability.

    Returns
    -------
    List[Union[str, int]]
        A list of labels corresponding to the skimmed sample groups. Returns an
        empty list if no groups are significantly different.

    Raises
    ------
    ValueError
        If fewer than two samples are provided.

    Notes
    -----
    The function first applies a Kruskal-Wallis H-test to determine if there is
    a significant difference between any of the sample groups. If a significant
    difference is found, it proceeds to rank the sample groups and uses
    multiple Mann-Whitney U-tests to skim the lowest ranked groups, adjusting
    the significance level (`alpha`) for multiple comparisons according to a
    sequential Holm-Bonferroni program.

    Examples
    --------
    >>> samples = [[1, 2, 3, 4, 5], [2, 3, 4, 4, 4], [8, 9, 7, 6, 4]]
    >>> labels = ['Group 1', 'Group 2', 'Group 3']
    >>> skim_lowest(samples, labels)
    ['Group 1']
    """
    try:
        return _do_skim_lowest(
            samples,
            labels,
            alpha=alpha,
            min_obs=min_obs,
            nan_policy=nan_policy,
            reverse=reverse,
        )
    except ValueError as e:
        warnings.warn(f"ValueError `{e}` ocurred. No groups skimmed.")
        return []

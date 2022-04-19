def eps_growth_rate(eps_final: float, eps_initial: float, n: int) -> float:
    """Calculate the earnings growth rate, otherwise known as Earnings Per Share growth
    rate (EPS CAGR).

    EPS Growth rate = ((EPSfinal / EPSinitial)^1/n - 1) * 100%

    Example:
        EPS2019 = $2.32 USD
        EPS2020 = $3.00 USD
        EPS2021 = $2.99 USD
        EPS2022 = $3.31 USD

        EPS Growth rate = ((EPS2019 / EPS2021)^1/3 - 1) * 100%,
        EPS Growth rate = 8.82%

    Args:
        eps_final (float): Previous period's revenue.
        eps_initial (float): Current period's revenue.
        n (int): Number of periods.

    Returns:
        float: The EPS Growth rate.
    """
    return ((eps_final / eps_initial) ** (1 / n) - 1) * 100

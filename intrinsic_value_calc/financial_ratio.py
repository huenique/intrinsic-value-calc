"""
Intrinsic Value (IV) analysis based on a financial metric.
"""
from intrinsic_value_calc.formulas import eps_growth_rate


def iv_by_pe_ratio(eps: float, r: float, pe_ratio: float) -> float:
    """Get the stock's intrinsic value using P/E ratio.

    Intrinsic value = Earnings per share (EPS) x (1 + r) x P/E ratio
    where r = the expected earnings growth rate

    Example: ($3.30 per share) x (1 + 0.125) x 35.5 = $131.79 per share

    Args:
        eps (float): The earnings per share.
        r (float): The expected earnings growth rate.
        pe_ratio (float): The price/earnings ratio.

    Returns:
        float: The stock's intrinsic value.
    """
    return (eps) * (1 + r) * pe_ratio


def main():
    # https://edge.pse.com.ph/openDiscViewer.do?edge_no=a878e6cd6b389d273470cea4b051ca8f
    eps = 173.18  # Earnings/(Loss) Per Share (Basic)
    r = eps_growth_rate(173.18, 135.04, 2) / 100
    pe_ratio = 15.022  # Price/Earnings Ratio
    intrinsic_value = iv_by_pe_ratio(eps, r, pe_ratio)
    print(intrinsic_value)


if __name__ == "__main__":
    main()

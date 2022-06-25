class Income:
    """
    Class representing salary income, has attributes for income over different time ranges.

    Income can be initialised with annual or monthly income amount.
    """

    def __init__(self, annual: float = None, monthly: float = None, hours: float = 40):
        """

        Args:
            annual: annual income
            monthly: monthly income
            hours: number of working hours in a week, used to calculate hourly income.
        """
        self.set_hours(hours)
        self._set_factors()
        if annual:
            amount = float(annual)
            factor = float(12)
        if monthly:
            amount = float(monthly)
            factor = float(1)

    def _set_factors(self):
        self.factors = dict(
            annual=12,
            monthly=1,
            weekly=float(12) / 52,
            daily=float(12) / (52 * 7),
            hourly=float(12) / (52 * 7 * self.hours),
        )

    def _normalise(self):


    def set_hours(self, hours):
        self.hours = hours
        self._set_factors()

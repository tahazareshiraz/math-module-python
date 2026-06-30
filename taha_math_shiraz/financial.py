from .power import pow_, log


def simple_interest(principal, rate, time):
    return principal * rate * time


def compound_interest(principal, rate, periods_per_year, years):
    return principal * pow_(1 + rate / periods_per_year, periods_per_year * years) - principal


def compound_amount(principal, rate, periods_per_year, years):
    return principal * pow_(1 + rate / periods_per_year, periods_per_year * years)


def continuous_compound_amount(principal, rate, years):
    from .power import exp
    return principal * exp(rate * years)


def present_value(future_value, rate, periods):
    return future_value / pow_(1 + rate, periods)


def future_value(present_value_amount, rate, periods):
    return present_value_amount * pow_(1 + rate, periods)


def annuity_present_value(payment, rate, periods):
    if rate == 0:
        return payment * periods
    return payment * (1 - pow_(1 + rate, -periods)) / rate


def annuity_future_value(payment, rate, periods):
    if rate == 0:
        return payment * periods
    return payment * (pow_(1 + rate, periods) - 1) / rate


def loan_payment(principal, rate, periods):
    if rate == 0:
        return principal / periods
    return principal * rate / (1 - pow_(1 + rate, -periods))


def net_present_value(rate, cash_flows):
    total = 0.0
    for t, cash_flow in enumerate(cash_flows):
        total += cash_flow / pow_(1 + rate, t)
    return total


def internal_rate_of_return(cash_flows, guess=0.1, iterations=1000, tolerance=1e-9):
    rate = guess
    for _ in range(iterations):
        npv = net_present_value(rate, cash_flows)
        derivative = 0.0
        for t, cash_flow in enumerate(cash_flows):
            if t > 0:
                derivative -= t * cash_flow / pow_(1 + rate, t + 1)
        if derivative == 0:
            break
        new_rate = rate - npv / derivative
        if abs(new_rate - rate) < tolerance:
            return new_rate
        rate = new_rate
    return rate


def doubling_time(rate):
    return log(2) / log(1 + rate)


def effective_annual_rate(nominal_rate, periods_per_year):
    return pow_(1 + nominal_rate / periods_per_year, periods_per_year) - 1


def discount_factor(rate, periods):
    return 1.0 / pow_(1 + rate, periods)


def amortization_schedule(principal, rate, periods):
    payment = loan_payment(principal, rate, periods)
    balance = principal
    schedule = []
    for period in range(1, periods + 1):
        interest_payment = balance * rate
        principal_payment = payment - interest_payment
        balance -= principal_payment
        schedule.append({
            "period": period,
            "payment": payment,
            "principal": principal_payment,
            "interest": interest_payment,
            "balance": max(balance, 0.0),
        })
    return schedule


def break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit):
    denom = price_per_unit - variable_cost_per_unit
    if denom <= 0:
        raise ValueError("price must exceed variable cost")
    return fixed_costs / denom


def markup_percentage(cost, selling_price):
    if cost == 0:
        raise ValueError("cost must not be zero")
    return (selling_price - cost) / cost * 100


def profit_margin(revenue, cost):
    if revenue == 0:
        raise ValueError("revenue must not be zero")
    return (revenue - cost) / revenue * 100


def compound_annual_growth_rate(beginning_value, ending_value, years):
    if beginning_value <= 0 or years <= 0:
        raise ValueError("invalid input for CAGR")
    return pow_(ending_value / beginning_value, 1.0 / years) - 1

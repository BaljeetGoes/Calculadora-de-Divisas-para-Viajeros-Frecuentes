def exchange_money(bugdet:float, exchange_rate:float) -> float:
        return bugdet / exchange_rate

total = exchange_money(300, 0.0075)

print(f"Su total es de: {total:.1f}")
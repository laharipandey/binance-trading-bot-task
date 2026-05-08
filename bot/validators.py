def validate_inputs(symbol, side, order_type, quantity, price):
    if not symbol:
        return False, "Symbol is required."
    if side not in ['BUY', 'SELL']:
        return False, "Side must be BUY or SELL."
    if order_type not in ['MARKET', 'LIMIT']:
        return False, "Type must be MARKET or LIMIT."
    if quantity <= 0:
        return False, "Quantity must be greater than 0."
    if order_type == 'LIMIT' and (price is None or price <= 0):
        return False, "Price is required for LIMIT orders."
    return True, ""
import click
from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

logger = setup_logging()

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', type=click.Choice(['BUY', 'SELL']), required=True)
@click.option('--type', 'order_type', type=click.Choice(['MARKET', 'LIMIT']), required=True)
@click.option('--qty', type=float, required=True)
@click.option('--price', type=float)
def main(symbol, side, order_type, qty, price):
    is_valid, error_msg = validate_inputs(symbol, side, order_type, qty, price)
    if not is_valid:
        click.echo(f"Error: {error_msg}")
        return

    bot = BinanceFuturesClient()
    logger.info(f"Placing {side} {order_type} for {symbol}")

    try:
        response = bot.place_order(symbol, side, order_type, qty, price)
        click.echo(f"Success! Order ID: {response.get('orderId')}")
        logger.info(f"Response: {response}")
    except Exception as e:
        click.echo(f"Failed: {str(e)}")
        logger.error(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
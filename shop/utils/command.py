
from shop.handlers import (
    handle_add_command,
    handle_remove_command,
    handle_search_command,
    handle_show_command,
    handle_total_price_command,
)

COMMANDS = {
    'add': handle_add_command,
    'show': handle_show_command,
    'remove': handle_remove_command,
    'search': handle_search_command,
    'price': handle_total_price_command,
}



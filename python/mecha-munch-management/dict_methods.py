"""Functions to manage a users shopping cart items."""

from typing import Iterable


def add_item(
    current_cart: dict[str, int], items_to_add: Iterable[str]
) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return add_item({}, notes)  # dict.fromKeys(notes, 1)


def update_recipes(
    ideas: dict[str, dict[str, int]], recipe_updates: tuple[tuple[str, dict[str, int]]]
) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas |= recipe_updates  # ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(
    cart: dict[str, int], isle_mapping: dict[str, list]
) -> dict[str, list]:
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for key in isle_mapping:
        isle_mapping[key].insert(0, cart[key])
    return dict(reversed(sorted(isle_mapping.items())))


def update_store_inventory(
    fulfillment_cart: dict[str, list], store_inventory: dict[str, list]
) -> dict[str, list]:
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key, value in fulfillment_cart.items():
        store_inventory[key][0] -= value[0]
        if not store_inventory[key][0]:
            store_inventory[key][0] = "Out of Stock"
    return store_inventory

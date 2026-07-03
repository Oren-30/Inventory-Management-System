from flask import Flask, jsonify, request, render_template

from inventory import (
    get_all_items,
    get_item,
    add_item,
    update_item,
    delete_item
)
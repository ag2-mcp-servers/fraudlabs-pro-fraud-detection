# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T19:16:56+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity

from models import Action, Format

app = MCPProxy(
    contact={'x-twitter': 'fraudlabspro'},
    description='Online payment fraud detection service. It helps merchants to minimize chargebacks and therefore maximize the revenue. It can be used to detect fraud for various kinds of payment method, such as credit card, paypal, cod and so on. Please visit https://www.fraudlabspro.com to learn more.',
    title='FraudLabs Pro Fraud Detection',
    version='1.1',
    servers=[
        {'description': 'FraudLabs Pro', 'url': 'https://api.fraudlabspro.com'},
        {
            'description': 'SwaggerHub API Auto Mocking',
            'url': 'https://virtserver.swaggerhub.com/fraudlabspro/fraudlabspro/1.0',
        },
    ],
)


@app.post(
    '/v1/order/feedback',
    description=""" Feedback the status of an order transaction. """,
    tags=['order_feedback_handling'],
)
def post_v1_order_feedback(
    id: str,
    key: str = ...,
    format: Optional[Format] = None,
    action: Action = ...,
    notes: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/order/screen',
    description=""" Screen order for payment fraud. """,
    tags=['order_processing_operations'],
)
def post_v1_order_screen(
    ip: str,
    key: str = ...,
    format: Optional[Format] = None,
    last_name: Optional[str] = None,
    first_name: Optional[str] = None,
    bill_addr: Optional[str] = None,
    bill_city: Optional[str] = None,
    bill_state: Optional[str] = None,
    bill_country: Optional[str] = None,
    bill_zip_code: Optional[str] = None,
    ship_addr: Optional[str] = None,
    ship_city: Optional[str] = None,
    ship_state: Optional[str] = None,
    ship_country: Optional[str] = None,
    ship_zip_code: Optional[str] = None,
    email_domain: Optional[str] = None,
    user_phone: Optional[str] = None,
    email: Optional[str] = None,
    email_hash: Optional[str] = None,
    username_hash: Optional[str] = None,
    password_hash: Optional[str] = None,
    bin_no: Optional[str] = None,
    card_hash: Optional[str] = None,
    avs_result: Optional[str] = None,
    cvv_result: Optional[str] = None,
    user_order_id: Optional[str] = None,
    user_order_memo: Optional[str] = None,
    amount: Optional[float] = None,
    quantity: Optional[int] = None,
    currency: Optional[str] = None,
    department: Optional[str] = None,
    payment_mode: Optional[str] = None,
    flp_checksum: Optional[str] = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)

from typing import Union

import requests

from .dataclasses import (
    APIResponse,
    Credential,
    IPNResponse,
    IPNValidationStatus,
    OrderValidationPostData,
    OrderValidationResponse,
    PaymentInitPostData,
    PaymentInitResponse,
    RefundInitiateResponse,
    RefundRequestPostData,
    RefundResponse,
    TransactionBySessionResponse,
    TransactionsByIDResponse,
)


class SSLCommerzClient:
    def __init__(self, store_id: str, store_passwd: str, sandbox: bool = False):
        self.store_id = store_id
        self.store_passwd = store_passwd
        self.sandbox = sandbox

    @property
    def baseURL(self):
        if self.sandbox:
            return "https://sandbox.sslcommerz.com"
        else:
            return "https://securepay.sslcommerz.com"

    @property
    def credential(self):
        return {
            "store_id": self.store_id,
            "store_passwd": self.store_passwd,
        }

    def initiate_session(self, postData: Union[PaymentInitPostData, dict]):
        """Initiates an session."""
        if not isinstance(postData, PaymentInitPostData):
            postData = PaymentInitPostData(**postData)
        url = self.baseURL + "/gwprocess/v4/api.php"
        request_data = postData.model_dump(exclude_none=True)
        request_data.update(self.credential)
        resp = requests.post(url, request_data)
        if resp:
            return APIResponse(
                raw_data=resp,
                status_code=resp.status_code,
                response=PaymentInitResponse(**resp.json()),
            )
        else:
            return APIResponse(raw_data=resp, status_code=resp.status_code)

    def validate_IPN(self, data: dict):
        """Validate an IPN response."""
        ipnResponse = IPNResponse(**data)
        status = ipnResponse.validate_against_credential(
            credential=Credential(**self.credential)
        )
        return IPNValidationStatus(status=status, response=ipnResponse)

    def get_order_validation_data(
        self, data: Union[dict, OrderValidationPostData, IPNResponse]
    ):
        """Get Order validation data from API."""
        if isinstance(data, IPNResponse):
            data = OrderValidationPostData(val_id=data.val_id)
        elif not isinstance(data, OrderValidationPostData):
            data = OrderValidationPostData(**data)
        url = self.baseURL + "/validator/api/validationserverAPI.php"
        request_data = data.model_dump(exclude_none=True)
        request_data.update(self.credential)
        resp = requests.get(url, request_data)
        if resp:
            return APIResponse(
                raw_data=resp,
                status_code=resp.status_code,
                response=OrderValidationResponse(**resp.json()),
            )
        else:
            return APIResponse(raw_data=resp, status_code=resp.status_code)

    def initiate_refund(self, data: Union[dict, RefundRequestPostData]):
        """Initiate a refund."""
        if not isinstance(data, RefundRequestPostData):
            data = RefundRequestPostData(**data)
        url = self.baseURL + "/validator/api/merchantTransIDvalidationAPI.php"
        request_data = data.model_dump(exclude_none=True)
        request_data.update(self.credential)
        resp = requests.get(url, params=request_data)
        if resp:
            return APIResponse(
                raw_data=resp,
                status_code=resp.status_code,
                response=RefundInitiateResponse(**resp.json()),
            )
        else:
            return APIResponse(raw_data=resp, status_code=resp.status_code)

    def get_refund_data(self, refund_ref_id: str):
        """Get existing refund data."""
        url = self.baseURL + "/validator/api/merchantTransIDvalidationAPI.php"
        request_data = {"refund_ref_id": refund_ref_id, **self.credential}
        resp = requests.get(url, request_data)
        if resp:
            return APIResponse(
                raw_data=resp,
                status_code=resp.status_code,
                response=RefundResponse(**resp.json()),
            )
        else:
            return APIResponse(raw_data=resp, status_code=resp.status_code)

    def get_transaction_by_session(self, sessionkey: str):
        """Get a transaction by sessionkey."""
        url = self.baseURL + "/validator/api/merchantTransIDvalidationAPI.php"
        request_data = {"sessionkey": sessionkey, **self.credential}
        resp = requests.get(url, request_data)
        if resp:
            return APIResponse(
                raw_data=resp,
                status_code=resp.status_code,
                response=TransactionBySessionResponse(**resp.json()),
            )
        else:
            return APIResponse(raw_data=resp, status_code=resp.status_code)

    def get_transaction_by_id(self, tran_id: str):
        """Get transactions by transaction id."""
        url = self.baseURL + "/validator/api/merchantTransIDvalidationAPI.php"
        request_data = {"tran_id": tran_id, **self.credential}
        resp = requests.get(url, request_data)
        if resp:
            return APIResponse(
                raw_data=resp,
                status_code=resp.status_code,
                response=TransactionsByIDResponse(**resp.json()),
            )
        else:
            return APIResponse(raw_data=resp, status_code=resp.status_code)

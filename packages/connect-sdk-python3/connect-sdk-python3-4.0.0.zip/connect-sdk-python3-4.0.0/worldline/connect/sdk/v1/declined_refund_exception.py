#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from typing import Optional

from .declined_transaction_exception import DeclinedTransactionException
from worldline.connect.sdk.v1.domain.refund_error_response import RefundErrorResponse
from worldline.connect.sdk.v1.domain.refund_result import RefundResult


class DeclinedRefundException(DeclinedTransactionException):
    """
    Represents an error response from a refund call.
    """

    def __init__(self, status_code: int, response_body: str, errors: Optional[RefundErrorResponse]):
        if errors is not None:
            super(DeclinedRefundException, self).__init__(status_code, response_body, errors.error_id, errors.errors,
                                                          DeclinedRefundException.__create_message(errors))
        else:
            super(DeclinedRefundException, self).__init__(status_code, response_body, None, None,
                                                          DeclinedRefundException.__create_message(errors))
        self.__errors = errors

    @staticmethod
    def __create_message(errors: Optional[RefundErrorResponse]) -> str:
        if errors is not None:
            refund = errors.refund_result
        else:
            refund = None
        if refund is not None:
            return "declined refund '" + refund.id + "' with status '" + refund.status + "'"
        else:
            return "the Worldline Global Collect platform returned a declined refund response"

    @property
    def refund_result(self) -> Optional[RefundResult]:
        """
        :return: The result of creating a refund if available, otherwise None.
        """
        if self.__errors is None:
            return None
        else:
            return self.__errors.refund_result

# Copyright ©, 2022-present, Lightspark Group, Inc. - All Rights Reserved

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from uma.JSONable import JSONable
from uma.kyc_status import KycStatus


@dataclass
class PayerDataOptions(JSONable):
    name_required: bool
    email_required: bool
    compliance_required: bool

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identifier": {"mandatory": True},
            "name": {"mandatory": self.name_required},
            "email": {"mandatory": self.email_required},
            "compliance": {"mandatory": self.compliance_required},
        }

    @classmethod
    def _from_dict(cls, json_dict: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "name_required": json_dict["name"]["mandatory"],
            "email_required": json_dict["email"]["mandatory"],
            "compliance_required": json_dict["compliance"]["mandatory"],
        }


@dataclass
class CompliancePayerData(JSONable):
    kyc_status: KycStatus
    """KYC information about the sender."""

    utxos: List[str]
    """The list of UTXOs of the sender's channels that might be used to forward the payment"""

    node_pubkey: Optional[str]
    """The public key of the sender's node that will be used to send the payment"""

    encrypted_travel_rule_info: Optional[str]
    """The travel rule information of the sender. This is encrypted with the receiver's public encryption key"""

    travel_rule_format: Optional[str]
    """
    An optional standardized format of the travel rule information (e.g. IVMS). Null indicates raw json or a custom format.
    This field is formatted as <standardized format>@<version> (e.g. ivms@101.2023). Version is optional.
    """

    signature: str
    """Signature is the base64-encoded signature of sha256(ReceiverAddress|Nonce|Timestamp)"""

    signature_nonce: str

    signature_timestamp: int
    """Time stamp of the signature in seconds"""

    utxo_callback: str
    """The URL that the receiver will call to send UTXOs of the channels that receiver used to receive the payment the once it completes."""

    @classmethod
    def _get_field_name_overrides(cls) -> Dict[str, str]:
        return {"node_pubkey": "nodePubKey"}


@dataclass
class PayerData(JSONable):
    identifier: str
    name: Optional[str]
    email: Optional[str]
    compliance: Optional[CompliancePayerData]

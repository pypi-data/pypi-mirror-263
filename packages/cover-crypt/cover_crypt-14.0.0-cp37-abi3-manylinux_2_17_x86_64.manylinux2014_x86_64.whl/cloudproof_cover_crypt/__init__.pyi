from typing import List, Optional, Tuple, Union

class Attribute:
    """An attribute in a policy group is characterized by the axis policy name
    and its unique name within this axis.

    Args:
        axis (str): policy axis the attributes belongs to
        name (str): unique attribute name within this axis
    """

    def __init__(self, axis: str, name: str): ...
    def get_axis(self) -> str:
        """Get the corresponding axis of the attribute.

        Returns:
            str
        """
    def get_name(self) -> str:
        """Get the attribute name.

        Returns:
            str
        """
    def to_string(self) -> str:
        """Creates a string representation of the attribute.

        Returns:
            str
        """
    @staticmethod
    def from_string(string: str) -> Attribute:
        """Creates a policy attribute from a string representation.

        Args:
            string (str): Attribute in string format

        Returns:
            Attribute
        """

class PolicyAxis:
    """Defines an unique policy axis with the given name and attribute names.
    If `hierarchical` is set to `true`, the axis is defined as hierarchical.

    Args:
            name (str): axis name
            attributes (List[Union[str, Tuple[str, bool]]]): properties of the attributes:

                - name of the attribute
                - boolean to activate post quantum encryption on this attribute
            hierarchical (bool): set the axis to be hierarchical
    """

    def __init__(
        self,
        name: str,
        attributes: List[Union[str, Tuple[str, bool]]],
        hierarchical: bool,
    ): ...
    def len(self) -> int:
        """Returns the number of attributes belonging to this axis.

        Returns:
            int
        """
    def is_empty(self) -> bool:
        """Check whether the attribute list is empty.

        Returns:
            bool
        """
    def get_name(self) -> str:
        """Get axis name.

        Returns:
            str
        """
    def get_attributes(self) -> List[str]:
        """Get the list of attributes in the axis.

        Returns:
            List[str]
        """
    def is_hierarchical(self) -> bool:
        """Check whether the axis is hierarchical.

        Returns:
            bool
        """
    def to_string(self) -> str:
        """Creates a string representation of the policy axis.

        Returns:
            str
        """

class Policy:
    """A policy is a set of policy axes. A fixed number of attribute creations
    (revocations + additions) is allowed.
    """

    def __init__(self): ...
    def add_axis(self, axis: PolicyAxis) -> None:
        """Adds the given policy axis to the policy.

        Args:
            axis (PolicyAxis)
        """
    def remove_axis(self, axis_name: str) -> None:
        """Removes the given axis from the policy.
        Fails if there is no such axis in the policy.

            Args:
                axis_name (str)
        """
    def add_attribute(self, attribute: Attribute, is_hybridized: bool) -> None:
        """Adds the given attribute to the policy.
        Fails if the axis of the attribute does not exist in the policy.

            Args:
                attribute (Attribute): The name and axis of the new attribute.
                is_hybridized (bool): Whether to use post quantum keys for this attribute
        """
    def remove_attribute(self, attribute: Attribute) -> None:
        """Removes the given attribute from the policy.
        Encrypting and decrypting for this attribute will no longer be possible once the keys are updated.

            Args:
                attribute (Attribute)
        """
    def disable_attribute(self, attribute: Attribute) -> None:
        """Marks an attribute as read only.
        The corresponding attribute key will be removed from the public key.
        But the decryption key will be kept to allow reading old ciphertext.

            Args:
                attribute (Attribute)
        """
    def rename_attribute(self, attribute: Attribute, new_name: str) -> None:
        """Changes the name of an attribute.

        Args:
            attribute (Attribute)
            new_name (str)
        """
    def attributes(self) -> List[Attribute]:
        """Returns the list of Attributes of this Policy.

        Returns:
            List[Attribute]
        """
    def attribute_values(self, attribute: Attribute) -> List[int]:
        """Returns the list of all attributes values given to an attribute
        over the time after rotations. The current value is returned first

        Args:
            attribute (Attribute)

        Returns:
            List[int]
        """
    def attribute_current_value(self, attribute: Attribute) -> int:
        """Retrieves the current value of an attribute.

        Args:
            attribute (Attribute)

        Returns:
            int
        """
    def to_bytes(self) -> bytes:
        """Formats policy to bytes.

        Returns:
            str
        """
    def deep_copy(self) -> Policy:
        """Performs deep copy of the policy.

        Returns:
            Policy
        """
    @staticmethod
    def from_bytes(policy_json: bytes) -> Policy:
        """Reads policy from bytes.

        Args:
            policy_json (str)

        Returns:
            Policy
        """

class MasterSecretKey:
    def to_bytes(self) -> bytes:
        """Converts key to bytes.

        Returns:
            bytes
        """
    @staticmethod
    def from_bytes(key_bytes: bytes) -> MasterSecretKey:
        """Reads key from bytes.

        Args:
            key_bytes (bytes)

        Returns:
            MasterSecretKey
        """

class MasterPublicKey:
    def to_bytes(self) -> bytes:
        """Converts key to bytes.

        Returns:
            bytes
        """
    @staticmethod
    def from_bytes(key_bytes: bytes) -> MasterPublicKey:
        """Reads key from bytes.

        Args:
            key_bytes (bytes)

        Returns:
            MasterPublicKey
        """

class UserSecretKey:
    def to_bytes(self) -> bytes:
        """Converts key to bytes.

        Returns:
            bytes
        """
    @staticmethod
    def from_bytes(key_bytes: bytes) -> UserSecretKey:
        """Reads key from bytes.

        Args:
            key_bytes (bytes)

        Returns:
            UserSecretKey
        """

class SymmetricKey:
    def to_bytes(self) -> bytes:
        """Converts key to bytes.

        Returns:
            bytes
        """
    @staticmethod
    def from_bytes(key_bytes: bytes) -> SymmetricKey:
        """Reads key from bytes.

        Args:
            key_bytes (bytes)

        Returns:
            SymmetricKey
        """

class CoverCrypt:
    """The engine is the main entry point for the core functionalities."""

    def __init__(self): ...
    def generate_master_keys(
        self, policy: Policy
    ) -> Tuple[MasterSecretKey, MasterPublicKey]:
        """Generate the master authority keys for supplied Policy.

        Args:
            policy (Policy): policy used to generate the keys

        Returns:
            Tuple[MasterSecretKey, MasterPublicKey]
        """
    def update_master_keys(
        self, policy: Policy, msk: MasterSecretKey, pk: MasterPublicKey
    ) -> None:
        """Update the master keys according to this new policy.

        Args:
            policy (Policy): policy used to generate the keys
            msk (MasterSecretKey): master secret key
            pk (MasterPublicKey): master public key
        """
    def rekey_master_keys(
        self,
        access_policy_str: str,
        policy: Policy,
        msk: MasterSecretKey,
        mpk: MasterPublicKey,
    ):
        """Generate new keys associated to the given access policy in the master keys.
        User keys will need to be refreshed after this step.

        Args:
            access_policy_str (str): describe the keys to renew
            policy (Policy): global policy
            msk (MasterSecretKey): master secret key
            mpk (MasterPublicKey): master public key
        """
    def prune_master_secret_key(
        self, access_policy_str: str, policy: Policy, msk: MasterSecretKey
    ):
        """Removes old keys associated to the given master keys from the master keys.
        This will permanently remove access to old ciphers.

        Args:
            access_policy_str (str): describe the keys to prune
            policy (Policy): global policy
            msk (MasterSecretKey): master secret key
        """
    def generate_user_secret_key(
        self, msk: MasterSecretKey, access_policy_str: str, policy: Policy
    ) -> UserSecretKey:
        """Generate a user secret key.
        A new user secret key does NOT include the old (i.e. rotated) partitions.

        Args:
            msk (MasterSecretKey): master secret key
            access_policy_str (str): user access policy
            policy (Policy): global policy

        Returns:
            UserSecretKey
        """
    def refresh_user_secret_key(
        self,
        usk: UserSecretKey,
        msk: MasterSecretKey,
        keep_old_accesses: bool,
    ):
        """Refreshes the user key according to the given master key.
        The user key will be granted access to the current partitions, as determined by its access policy.
        If `keep_old_accesses` is set, the user access to rotated partitions will be preserved

        Args:
            usk (UserSecretKey): the user key to refresh
            msk (MasterSecretKey): master secret key
            keep_old_accesses (bool): whether access to old partitions (i.e. before rotation) should be kept
        """
    def encrypt_symmetric_block(
        self,
        symmetric_key: SymmetricKey,
        plaintext: bytes,
        authentication_data: Optional[bytes] = ...,
    ) -> bytes:
        """Encrypts data symmetrically in a block.

        Args:
            symmetric_key (SymmetricKey): symmetric key
            plaintext (bytes): plaintext to encrypt
            authentication_data (Optional[bytes]): associated data to be passed to the DEM scheme

        Returns:
            bytes: ciphertext bytes
        """
    def decrypt_symmetric_block(
        self,
        symmetric_key: SymmetricKey,
        ciphertext: bytes,
        authentication_data: Optional[bytes] = ...,
    ) -> bytes:
        """Symmetrically decrypts encrypted data in a block.

        Args:
            symmetric_key (SymmetricKey): symmetric key
            ciphertext (bytes): ciphertext in bytes
            authentication_data (Optional[bytes]): associated data to be passed to the DEM scheme

        Returns:
            bytes: plaintext bytes
        """
    def encrypt_header(
        self,
        policy: Policy,
        access_policy_str: str,
        public_key: MasterPublicKey,
        header_metadata: Optional[bytes] = ...,
        authentication_data: Optional[bytes] = ...,
    ) -> Tuple[SymmetricKey, bytes]:
        """Generates an encrypted header. A header contains the following elements:
        - `encapsulation_size`  : the size of the symmetric key encapsulation (u32)
        - `encapsulation`       : symmetric key encapsulation using CoverCrypt
        - `encrypted_metadata`  : Optional metadata encrypted using the DEM

        Args:
            policy (Policy): global policy
            access_policy_str (str): access policy
            public_key (MasterPublicKey): CoverCrypt public key
            header_metadata (Optional[bytes]): additional data to encrypt with the header
            authentication_data (Optional[bytes]): authentication data to use in symmetric encryption

        Returns:
            Tuple[SymmetricKey, bytes]: (symmetric key, ciphertext bytes)
        """
    def decrypt_header(
        self,
        usk: UserSecretKey,
        encrypted_header_bytes: bytes,
        authentication_data: Optional[bytes] = ...,
    ) -> Tuple[SymmetricKey, bytes]:
        """Decrypts the given header bytes using a user decryption key.

        Args:
            usk (UserSecretKey): user secret key
            encrypted_header_bytes (bytes): encrypted header bytes
            authentication_data (Optional[bytes]): authentication data to use in symmetric decryption

        Returns:
            Tuple[SymmetricKey, bytes]: (symmetric key, plaintext bytes)
        """
    def encrypt(
        self,
        policy: Policy,
        access_policy_str: str,
        pk: MasterPublicKey,
        plaintext: bytes,
        header_metadata: Optional[bytes] = ...,
        authentication_data: Optional[bytes] = ...,
    ) -> bytes:
        """Hybrid encryption. Concatenates the encrypted header and the symmetric
        ciphertext.

        Args:
            policy (Policy): global policy
            access_policy_str (str): access policy
            pk (MasterPublicKey): CoverCrypt public key
            plaintext (bytes): plaintext to encrypt using the DEM
            header_metadata (Optional[bytes]): additional data to symmetrically encrypt in the header
            authentication_data (Optional[bytes]): authentication data to use in symmetric encryptions

        Returns:
            bytes: ciphertext bytes
        """
    def decrypt(
        self,
        usk: UserSecretKey,
        encrypted_bytes: bytes,
        authentication_data: Optional[bytes] = ...,
    ) -> Tuple[bytes, bytes]:
        """Hybrid decryption.

        Args:
            usk (UserSecretKey): user secret key
            encrypted_bytes (bytes): encrypted header || symmetric ciphertext
            authentication_data (Optional[bytes]): authentication data to use in symmetric decryptions

        Returns:
            Tuple[bytes, bytes]: (plaintext bytes, header metadata bytes)
        """

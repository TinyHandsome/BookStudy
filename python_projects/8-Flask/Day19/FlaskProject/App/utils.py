import base64


def make_data_secret(source):
    encode_content = base64.standard_b64encode(source.encode("utf-8")).decode("utf-8")
    add_content_encode_content = "CHKa2GFL1twhMDhEZVfDfU2DoZHCLZk" + encode_content + "qOq3kRIxs26rmRtsUTJvBn9Z"
    encode_content_twice = base64.standard_b64encode(add_content_encode_content.encode("utf-8")).decode("utf-8")

    return encode_content_twice

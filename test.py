from apitemplateio_lib import APITemplateIO

api_key = "<Your API Key>"

def test_pdf():
    template_id = "<your pdf template id>"
    data = {
        "name": "hello world"
    }
    save_to = "/home/dev/result.pdf"

    apitemplate = APITemplateIO(api_key)
    apitemplate.create_pdf(template_id, data, save_to)

def test_image():
    template_id = "<your image template id>"
    data = {
        "overrides": [
            {
                "name" : "text_1",
                "text" : "hello world",
            }
        ]
    }
    save_to_jpeg = "/home/dev/result.jpeg"
    save_to_png = "/home/dev/result.png"

    apitemplate = APITemplateIO(api_key)
    apitemplate.create_image(template_id, data, save_to_jpeg, save_to_png)

def test_account_information():
    apitemplate = APITemplateIO(api_key)
    print(apitemplate.get_account_information())

def test_list_templates():
    apitemplate = APITemplateIO(api_key)
    templates = apitemplate.list_templates()
    for t in templates:
        print(t)

if __name__ == "__main__":
    test_pdf()
    test_image()
    test_account_information()
    test_list_templates()


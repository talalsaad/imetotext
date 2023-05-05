from modle.getImage import ImageGetter

spreadsheet_id = "1Gy83YEg83ViSOvzrTPoJTYAWMPvjZQKb6pfCzhOZGVo"
api_key = "AIzaSyDTp8-iKb5JtAOk3-QfQSqgLbj4ohHBwyw"

image_getter = ImageGetter(spreadsheet_id, api_key)


images = image_getter
print(images.lists())

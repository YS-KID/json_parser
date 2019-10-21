import os
import json

def json_parser(name):
  a = open(name)
  b = json.load(a)

  labels = []

  for i, j in zip(b["shapes"], range(len(b["shapes"]))):
    rect = i["points"]
    size_y = rect[1][0] - rect[0][0]
    size_x = rect[1][1] - rect[0][1]
    centre_y = (rect[1][0] + rect[0][0]) / 2
    centre_x = (rect[1][1] + rect[0][1]) / 2
    label_class = i["label"].split("-")[0]
    label = { u"size": {
                 u"x": size_y,
                 u"y": size_x
              },
              u"label_type": u"box",
              u"label_class": label_class,
              u"object_id": j + 1,
              u"centre": {
                 u"x" : centre_y,
                 u"y" : centre_x
              }
            }
    labels.append(label)
  
  root, _ = os.path.splitext(name)
  image_filename = root.split("./")[1] + ".jpg"
  parsered_json = {"labels": labels,
                  "complete": None,
                  "image_filename": image_filename}
  
  parseredFileName = root + "__labels.json"
  c = open(parseredFileName, 'w')
  json.dump(parsered_json, c, indent=4)


if __name__ == "__main__":
  for curDir, dirs, files in os.walk("."):
    for f in files:
      fileName = os.path.join(curDir, f)
      root, ext = os.path.splitext(fileName)
      if ext == ".json" and not("__labels" in root):
        json_parser(fileName)


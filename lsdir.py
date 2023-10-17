import os
import mimetypes


class Directoryz:
    def __init__(self):
        self.id = 0

    def scan_dir(self, path, level=1):
        children = []
        item_count = 0
        # Loop to append all directories first
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                item_count += 1
                self.id = level * 100 + item_count
                children.append({
                    "id": self.id,
                    "name": item,
                    "type": "directory",
                    "path": item_path,
                    "children": self.scan_dir(item_path, level + 1)
                })
        # Now we loop to append all files
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if not os.path.isdir(item_path):
                item_count += 1
                self.id = level * 100 + item_count
                mime_type = mimetypes.guess_type(item_path)[0] 
                if mime_type and mime_type.startswith('text'):
                    with open(item_path, 'r', encoding='utf8') as f:
                        content = f.read()
                    children.append({
                        "id": self.id,
                        "name": item,
                        "type": "file",
                        "path": item_path,
                        "filetype": mime_type,
                        "content": content
                    })
                else:
                    children.append({
                        "id": self.id,
                        "name": item,
                        "type": "file",
                        "path": item_path,
                        "filetype": mime_type
                    })

        return children

    def scan_cwd(self):
        cwd = os.getcwd()
        result = {
            "id": 0,
            "name": os.path.basename(cwd),
            "type": "directory",
            "path": cwd,
            "children": self.scan_dir(cwd)
        }
        return result

    def count_levels(self, data, level=0):
        if 'children' in data:
            return max([self.count_levels(child, level + 1) for child in data['children']], default=level)
        return level

    def print_tree(self, data, indent=0, level=0, max_levels=None):
        if max_levels is not None and level > max_levels:
            return
        if data['type'] == 'directory':
            print(' ' * indent + str(data['id']) + ". " + data['name'] + '/')
            for child in data['children']:
                self.print_tree(child, indent + 2, level + 1, max_levels)
        else:
            print(' ' * indent + str(data['id']) + ". " + data['name'])

    def find_item_by_id(self, id, data):
        if data['id'] == id:
            return data
        if data['id'] != id and data['type'] == 'directory':
            for child in data['children']:
                result = self.find_item_by_id(id, child)
                if result:
                    return result
        return None

    def count_files(self, data):
        count = 0
        if data['type'] == 'file':
            count += 1
        elif data['type'] == 'directory':
            for child in data['children']:
                count += self.count_files(child)  
        return count

    def count_dirs(self, data):
        count = 0
        if data['type'] == 'directory':
            count += 1
            for child in data['children']:
                if child['type'] == 'directory': 
                    count += self.count_dirs(child)  
        return count

    def count_all(self, data):
        return self.count_files(data)+self.count_dirs(data)

if __name__ == '__main__':
    pass
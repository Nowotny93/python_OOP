class PhotoAlbum:

    PAGE_PHOTOS = 4
    SUCCESS = 'photo added successfully on page'
    FAILED = 'No more free slots'
    DASHES = f'{11 * "-"}\n'

    def __init__(self, pages: int):
        self.pages = int(pages)
        self.photos = [[] for _ in range(pages)]
        self.pindex = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages: int = int(photos_count) // cls.PAGE_PHOTOS
        return cls(pages)

    def is_space(self) -> bool:
        return self.pindex < self.pages and len(self.photos[self.pindex]) < self.PAGE_PHOTOS

    def page_new(self) -> int:
        if len(self.photos[self.pindex]) == self.PAGE_PHOTOS:
            self.pindex += 1
            return self.pindex

    def add_photo(self, label:str) -> str:
        if not self.is_space():
            return self.FAILED
        self.photos[self.pindex].append(str(label))
        p_added = f'{label} {self.SUCCESS} {self.pindex + 1} slot {len(self.photos[self.pindex])}'
        self.page_new()
        return p_added

    def display(self) -> str:
        displ = self.DASHES
        for _ in self.photos:
            if _:
                displ += "".join('[] ' for p in range(len(_))).strip()
                #print('displ', displ)
            displ += f'\n{self.DASHES}'
        return displ

album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
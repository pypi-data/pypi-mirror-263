import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")

class ImagePreviewCollection:
    """Dictionary-like class of previews.This is a subclass of Python's built-in dict type,
    used to store multiple image previews.
    """

    def clear(self):
        """Clear all previews."""
        ...

    def close(self):
        """Close the collection and clear all previews."""
        ...

    def load(
        self,
        name: typing.Optional[str],
        filepath: typing.Optional[typing.Union[bytes, str]],
        filetype: typing.Optional[str],
        force_reload: typing.Optional[bool] = False,
    ) -> "bpy.types.ImagePreview":
        """Generate a new preview from given file path.

        :param name: The name (unique id) identifying the preview.
        :type name: typing.Optional[str]
        :param filepath: The file path to generate the preview from.
        :type filepath: typing.Optional[typing.Union[bytes, str]]
        :param filetype: The type of file, needed to generate the preview in ['IMAGE', 'MOVIE', 'BLEND', 'FONT'].
        :type filetype: typing.Optional[str]
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
        :type force_reload: typing.Optional[bool]
        :rtype: 'bpy.types.ImagePreview'
        :return: The Preview matching given name, or a new empty one.
        """
        ...

    def new(self, name: typing.Optional[str]) -> "bpy.types.ImagePreview":
        """Generate a new empty preview.

        :param name: The name (unique id) identifying the preview.
        :type name: typing.Optional[str]
        :rtype: 'bpy.types.ImagePreview'
        :return: The Preview matching given name, or a new empty one.
        """
        ...

class ImagePreviewCollection:
    def clear(self):
        """

        :param self:
        :type self:
        """
        ...

    def close(self):
        """

        :param self:
        :type self:
        """
        ...

    def copy(self): ...
    def fromkeys(self): ...
    def get(self, key, default):
        """

        :param self:
        :type self:
        :param key:
        :type key:
        :param default:
        :type default:
        """
        ...

    def items(self): ...
    def keys(self): ...
    def load(self, name, path, path_type, force_reload):
        """

        :param self:
        :type self:
        :param name:
        :type name:
        :param path:
        :type path:
        :param path_type:
        :type path_type:
        :param force_reload:
        :type force_reload:
        """
        ...

    def new(self, name):
        """

        :param self:
        :type self:
        :param name:
        :type name:
        """
        ...

    def pop(self): ...
    def popitem(self):
        """

        :param self:
        :type self:
        """
        ...

    def setdefault(self, key, default):
        """

        :param self:
        :type self:
        :param key:
        :type key:
        :param default:
        :type default:
        """
        ...

    def update(self): ...
    def values(self): ...

def new() -> "ImagePreviewCollection":
    """

    :rtype: 'ImagePreviewCollection'
    :return: a new preview collection.
    """

    ...

def new(): ...
def remove(pcoll: typing.Optional["ImagePreviewCollection"]):
    """Remove the specified previews collection.

    :param pcoll: Preview collection to close.
    :type pcoll: typing.Optional['ImagePreviewCollection']
    """

    ...

def remove(pcoll): ...

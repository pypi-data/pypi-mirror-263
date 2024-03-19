#
# بسم الله الرحمن الرحیم
# اللهم صل علی محمد و آل محمد
# ---------------------------
# Created on Mon Mar 04 2024
#
# Copyright (c) 2024 Abolfazl Danayi
# adanayidet@gmail.com
#

def _e():
    raise Exception("This class is just a helper and can not be used")

class EZJinja:
    def __init__(self, *args, **kwargs) -> None:
        _e()

    def build_path_of(self, *path) -> str:
        _e()

    def clean(self):
        _e()

    def init(self):
        _e()

    def copy_static_folder(
        self,
        destination_folder: str = "static",
        exclude_extensions: T.Iterable = [],
        allow_extensions: T.Union[T.Iterable, None] = None,
    ):
        _e()

    def fetch_meta(self, meta_file_name: str) -> T.Union[dict, list]:
        _e()

    def export_template(
        self,
        template: str,
        output_path: T.Union[None, str] = None,
        post_process: callable = lambda x: x,
        *args,
        **kwargs,
    ):
        """Leave the output_path to None to use the template's path"""
        _e()

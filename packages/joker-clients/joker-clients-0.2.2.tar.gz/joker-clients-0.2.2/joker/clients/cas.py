#!/usr/bin/env python3
# coding: utf-8
from __future__ import annotations

import typing
import zipfile
import zlib
from dataclasses import dataclass
from functools import cached_property
from urllib.parse import urljoin

import requests

from joker.clients.utils import Pathlike


class MemberFile(typing.TypedDict):
    cid: str
    filename: str


@dataclass
class ContentAddressedStorageClient:
    base_url: str
    credential: dict
    outer_url: str = None

    @property
    def inner_url(self):
        return self.base_url

    def __post_init__(self):
        if self.outer_url is None:
            self.outer_url = self.base_url

    @property
    def _adhoc_session(self):
        sess = requests.session()
        url = urljoin(self.base_url, 'login')
        sess.post(url, data=self.credential)
        return sess

    @cached_property
    def session(self):
        return self._adhoc_session

    def save(self, content: bytes) -> str:
        url = urljoin(self.base_url, 'files')
        resp = self._adhoc_session.post(url, files={'file': content})
        return resp.json()['data']

    def load(self, cid: str) -> bytes:
        url = urljoin(self.base_url, f'files/{cid}')
        resp = requests.get(url)
        return resp.content

    def save_text(self, text: str) -> str:
        content = zlib.compress(text.encode('utf-8'), wbits=31)
        return self.save(content)

    def load_text(self, cid: str) -> str:
        content = self.load(cid)
        return zlib.decompress(content, wbits=31).decode('utf-8')

    def get_outer_url(self, cid: str, filename: str):
        if filename.startswith('.'):
            url = f'/files/{cid}{filename}'
        else:
            url = f'/files/{cid}?filename={filename}'
        return urljoin(self.outer_url, url)

    def create_archive(self, path: Pathlike, memberfiles: list[MemberFile]):
        with zipfile.ZipFile(path, "w") as zipf:
            for m in memberfiles:
                content = self.load(m['cid'])
                with zipf.open(m['filename'], 'w') as fout:
                    fout.write(content)

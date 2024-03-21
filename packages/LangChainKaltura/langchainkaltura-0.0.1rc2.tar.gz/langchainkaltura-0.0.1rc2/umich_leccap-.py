"""Loads Pages, Announcements, Assignments and Files from a Canvas Course site."""
import json
import requests
from typing import List
from langchain.docstore.document import Document
from canvas_langchain.canvas import CanvasLoader, LogStatement
from sourcesystems.models import IndexingResult
import logging

logger = logging.getLogger(__name__)

class UmichLeccapCanvasLoader(CanvasLoader):
    def __init__(self, api_url: str, api_key: str = "", course_id: int = 0, index_external_urls: bool = False, leccap_api_key: str = "", leccap_domain: str = "leccap-beta.engin.umich.edu"):
        if not leccap_api_key:
            raise ValueError("leccap_api_key not set")

        self.leccap_api_key = leccap_api_key
        self.leccap_domain = leccap_domain

        CanvasLoader.__init__(self, api_url, api_key, course_id, index_external_urls)

        if self.leccap_api_key == "":
            self.logMessage(message = "Please specify a leccap_api_key", level = 'DEBUG')

        self.errors = []
        self.progress = []

    def check_user_for_leccap_site(self, uniqname: str = "") -> bool:
        if self.leccap_api_key != "":
            api_url = f"https://{self.leccap_domain}/leccap_api/api/maizeyuser?key={self.leccap_api_key}&uniqname={uniqname}"

            try:
                # Index leccap recordings
                response = json.loads(requests.get(api_url).text)

                if "errors" in response and len(response["errors"]) > 0:
                    for error in response["errors"]:
                        self.logMessage(message = error, level = 'DEBUG')

                if "found_sites" in response:
                    return response["found_sites"]
            except json.decoder.JSONDecodeError:
                self.logMessage(message="leccap: Error decoding JSON", level='DEBUG')
            except requests.exceptions.ConnectionError:
                self.logMessage(message = f"leccap: Could not connect to the server at {self.leccap_domain}", level = 'DEBUG')

        return False

    def logMessage(self, message, level):
        if level == 'WARNING':
            self.errors.append(LogStatement(
                message = message,
                level = level
            ))

        self.progress.append(LogStatement(
            message = message,
            level = level
        ))

    def load(self) -> IndexingResult:
        """Load documents."""

        # override if we have any errors
        state = 'SUCCESS'

        try:
            canvas_docs = CanvasLoader.load(self)
            self.progress, self.errors = CanvasLoader.get_details(self, 'DEBUG')
        except Exception as exp:
            logger.exception('Exception occurred in CanvasLoader')
            state = 'FAILURE'
            self.progress, self.errors = CanvasLoader.get_details(self, 'DEBUG')

            return IndexingResult(state='FAILURE', progress=self.progress, errors=self.errors, exception=exp )

        leccap_docs = []
        if self.leccap_api_key:
            # connect to the lecture recording server to get connected lecture recording sites
            api_url = f"https://{self.leccap_domain}/leccap_api/api/maizey?key={self.leccap_api_key}&canvas_site_id={self.course_id}"

            self.logMessage(message="Checking for connected Lecture Recording sites", level="DEBUG")

            try:
                # Index leccap recordings
                response = json.loads(requests.get(api_url).text)

                # put errors in the errors array
                if "errors" in response and len(response['errors']) > 0:
                    for error in response['errors']:
                        self.logMessage(message=error, level='DEBUG')

                # put chunks in a doc array
                if "captions" in response and len(response['captions']) > 0:
                    for caption in response['captions']:
                        for chunk in caption['chunks']:
                            leccap_docs.append(Document(
                                page_content=chunk['words'],
                                metadata={"source": f"{caption['recording_link']}?start={chunk['start_time']}", "filename": caption['recording_name'], "site_name": caption['site_name']}
                            ))
            except json.decoder.JSONDecodeError:
                self.logMessage(message="leccap: Error decoding JSON", level='DEBUG')
            except requests.exceptions.ConnectionError:
                self.logMessage(message=f"leccap: Could not connect to the server at {self.leccap_domain}", level='DEBUG')
            except Exception as exp:
                logger.exception('Exception occurred in CanvasLoader, lecture capture part')
                state = 'FAILURE'
                return IndexingResult(state='FAILURE', progress=self.progress, errors=self.errors, exception=exp )

        if len(self.errors) > 0:
            state = 'WARN'

        return IndexingResult(state=state, progress=self.progress, errors=self.errors, docs=canvas_docs + leccap_docs)

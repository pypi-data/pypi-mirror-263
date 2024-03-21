import os
import requests
import aiohttp
import mimetypes
from aiohttp import FormData
from dataclasses import dataclass
from typing import Optional, List, Union
from trufflepig._constants import SERVER_ADDRESS


@dataclass
class SearchResult:
    """
    Result of a search.

    Attributes:
        content (str): Content of the search result.
        citation (str): Source document from which the content originated.
        score (float): Similarity score to search query.
    """

    content: str
    citation: str
    score: float


@dataclass
class UploadTrackingResult:
    """
    The tracking status of a data upload request.

    Attributes:
        tracking_id (str): The upload job's tracking id.
        job_status (str): The status of an upload job (IN PROGRESS, SUCCESS, FAILED)
        start_time (int): The epoch timestamp of the initial upload request.
        end_time (str): The epoch timestamp of when the upload request reached a terminal state.
    """

    tracking_id: str
    job_status: str
    start_time: int
    end_time: int


class Index:
    def __init__(self, api_key: str, index_name: str):
        """
        Initialize a new Index object for interacting with an existing trufflepig search index.

        Parameters:
        -----------
        api_key: str
            The API key to be used for authenticating requests made using the trufflepig client.
        index_name: str
            The name of the index being accessed.

        Example:
        -----------
        index = Index("my-api-key", "my-index")
        """
        self.index_name = index_name
        self._api_key = api_key

    def __str__(self):
        return f"Index(index_name={self.index_name})"

    def upload(
        self,
        text: Union[Optional[List[str]], Optional[str]] = None,
        files: Union[Optional[List[str]], Optional[str]] = None,
    ) -> List[str]:
        """
        Upload data to your trufflepig index!

        Currently supported data types:
        - strings
        - files with the following mimetypes:
            - application/pdf
            - text/plain

        Parameters:
        -----------
        text: Union[Optional[List[str]], Optional[str]]
            Plaintext string data to be uploaded to the search index.
        files: Union[Optional[List[str]], Optional[str]]
            One or more names of files to be uploaded to the search index.

        Returns:
        -----------
        List[str]: A list of tracking ids for the upload job(s).

        Example:
        -----------
        tracking_ids = index.upload(files='somefile.pdf')
        """
        if (text and files and len(files) > 0) or (
            not text and (not files or len(files) == 0)
        ):
            raise ValueError("Must set one and only one of text or files.")
        if files and len(files) > 0:
            file_paths: List[str] = []
            if isinstance(files, str):
                file_paths = [files]
            elif isinstance(files, list):
                file_paths = files
            else:
                raise ValueError("Files must be either a list of strings or a string.")

            file_list = []
            for file_path in file_paths:
                if not os.path.isfile(file_path):
                    raise ValueError(f"Invalid file path: {file_path}")

                file_name = os.path.basename(file_path)
                mime_type = mimetypes.guess_type(file_path)[0]

                file_list.append(
                    ("files", (file_name, open(file_path, "rb"), mime_type))
                )

            response = requests.post(
                f"http://{SERVER_ADDRESS}/v0/indexes/{self.index_name}/upload",
                headers={"x-api-key": self._api_key},
                files=file_list,
            )

            for _, file_tuple in file_list:
                file_tuple[1].close()

            if response.status_code == 200:
                return response.json()["tracking_ids"]
            else:
                raise Exception(f"{response.status_code} Error: {response.text()}")

        if text:
            if isinstance(text, str):
                text = [text]
            elif not isinstance(text, list):
                raise ValueError("Data must be either a list of strings or a string.")

            json_data = {"text": text}
            response = requests.post(
                f"http://{SERVER_ADDRESS}/v0/indexes/{self.index_name}/upload",
                json=json_data,
                headers={"x-api-key": self._api_key},
            )
            if response.status_code == 200:
                return response.json()["tracking_ids"]
            else:
                raise Exception(f"{response.status_code} Error: {response.text}")

    def search(
        self, query_text: str, max_results: Optional[int] = 5
    ) -> List[SearchResult]:
        """
        Search your trufflepig index for relevant data!

        Parameters:
        -----------
        query_text: str
            A search query.
        max_results: Optional[int] = 5
            Maximum number of relevant results to be returned.

        Returns:
        -----------
        List[SearchResult]: A list of search result objects.

        Example:
        -----------
        search_results = index.search(query_text='What is a truffle pig?', max_results=2)
        """
        url = f"http://{SERVER_ADDRESS}/v0/indexes/{self.index_name}/search"
        headers = {"x-api-key": self._api_key}
        params = {"query_text": query_text, "max_results": max_results}

        response = requests.post(url, params=params, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            return [
                SearchResult(
                    content=item["content"],
                    citation=item["citation"],
                    score=item["score"],
                )
                for item in response_json
            ]
        else:
            raise Exception(f"{response.status_code} Error: {response.content}")

    def get_upload_status(self, tracking_ids: List[str]) -> List[UploadTrackingResult]:
        """
        Fetch statuses of upload jobs by tracking_ids provided in upload response.

        Parameters:
        -----------
        tracking_ids: List[str]
             A list of tracking ids corresponding to upload jobs.

        Returns:
        -----------
        List[UploadTrackingResult]: list of UploadTrackingResult dataclass.

        Example:
        -----------
        tracking_results = client.get_upload_status(["tracking_id_1"])
        print(tracking_results.status)
        """
        if len(tracking_ids) < 1:
            raise ValueError("must provide at least 1 tracking id.")

        # send http request
        response = requests.post(
            f"http://{SERVER_ADDRESS}/v0/upload_status",
            headers={"x-api-key": self._api_key},
            json={"tracking_ids": tracking_ids},
        )

        if response.status_code == 200:
            result = response.json()
            return [
                UploadTrackingResult(
                    tracking_id=item["tracking_id"],
                    job_status=item["job_status"],
                    start_time=item["start_time"],
                    end_time=item["end_time"],
                )
                for item in result
            ]
        else:
            raise Exception(f"{response.status_code} Error: {response.text}")

    async def upload_async(
        self,
        text: Union[Optional[List[str]], Optional[str]] = None,
        files: Union[Optional[List[str]], Optional[str]] = None,
    ) -> List[str]:
        """
        Asynchronously upload data to your trufflepig index!

        Currently supported data types:
        - strings
        - files with the following mimetypes:
            - application/pdf
            - text/plain

        Parameters:
        -----------
        text: Union[Optional[List[str]], Optional[str]]
            Plaintext string data to be uploaded to the search index.
        files: Union[Optional[List[str]], Optional[str]]
            One or more names of files to be uploaded to the search index.

        Returns:
        -----------
        List[str]: A list of tracking ids for the upload job(s).

        Example:
        -----------
        tracking_ids = await index.upload(files='somefile.pdf')
        """
        if (text and files and len(files) > 0) or (
            not text and (not files or len(files) == 0)
        ):
            raise ValueError("Must set one and only one of text or files.")

        if files and len(files) > 0:
            file_paths: List[str] = []

            if isinstance(files, str):
                file_paths = [files]
            elif isinstance(files, list):
                file_paths = files
            else:
                raise ValueError("Files must be either a list of strings or a string.")

            open_files = []  # List to keep track of opened file objects
            try:
                async with aiohttp.ClientSession() as session:
                    data = FormData()
                    for file_path in file_paths:
                        if not os.path.isfile(file_path):
                            raise ValueError(f"Invalid file path: {file_path}")

                        file_name = os.path.basename(file_path)
                        mime_type = (
                            mimetypes.guess_type(file_path)[0]
                            or "application/octet-stream"
                        )

                        f = open(file_path, "rb")  # Manually open the file
                        open_files.append(
                            f
                        )  # Add the file object to the list to keep track of it
                        data.add_field(
                            "files", f, filename=file_name, content_type=mime_type
                        )

                    async with session.post(
                        f"http://{SERVER_ADDRESS}/v0/indexes/{self.index_name}/upload",
                        headers={"x-api-key": self._api_key},
                        data=data,
                    ) as response:
                        if response.status == 200:
                            return (await response.json())["tracking_ids"]
                        else:
                            raise Exception(
                                f"{response.status} Error: {await response.text()}"
                            )
            finally:
                for f in open_files:  # Ensure all opened files are closed
                    f.close()

        if text:
            json_data = {"text": text}
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"http://{SERVER_ADDRESS}/v0/indexes/{self.index_name}/upload",
                    json=json_data,
                    headers={"x-api-key": self._api_key},
                ) as response:
                    if response.status == 200:
                        return (await response.json())["tracking_ids"]
                    else:
                        raise Exception(
                            f"{response.status} Error: {await response.text()}"
                        )

    async def search_async(
        self,
        query_text: str,
        max_results: Optional[int] = 5,
    ):
        """
        Asynchronously search your trufflepig index for relevant data!

        Parameters:
        -----------
        query_text: str
            A search query.
        max_results: Optional[int] = 5
            Maximum number of relevant results to be returned.

        Returns:
        -----------
        List[SearchResult]: A list of search result objects.

        Example:
        -----------
        search_results = await index.search(query_text='What is a truffle pig?', max_results=2)
        """
        url = f"http://{SERVER_ADDRESS}/v0/indexes/{self.index_name}/search"
        params = {"query_text": query_text, "max_results": max_results}

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers={"x-api-key": self._api_key}, params=params
            ) as response:
                if response.status == 200:
                    return [
                        SearchResult(
                            content=item["content"],
                            citation=item["citation"],
                            score=item["score"],
                        )
                        for item in await response.json()
                    ]
                else:
                    raise Exception(f"{response.status} Error: {await response.text()}")

    async def get_upload_status_async(
        self, tracking_ids: List[str]
    ) -> List[UploadTrackingResult]:
        """
        Asynchronously fetch statuses of upload jobs by tracking_ids provided in upload response.

        Parameters:
        -----------
        tracking_ids: List[str]
            A list of tracking ids corresponding to upload jobs.

        Returns:
        -----------
        List[UploadTrackingResult]: list of UploadTrackingResult dataclass.

        Example:
        -----------
        tracking_results = await client.get_upload_status(["tracking_id_1"])
        print(tracking_results.status)
        """
        if len(tracking_ids) < 1:
            raise ValueError("must provide at least 1 tracking id.")

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"http://{SERVER_ADDRESS}/v0/upload_status",
                headers={"x-api-key": self._api_key},
                json={"tracking_ids": tracking_ids},
            ) as response:
                if response.status == 200:
                    response_json = await response.json()
                    return [
                        UploadTrackingResult(
                            tracking_id=item["tracking_id"],
                            job_status=item["job_status"],
                            start_time=item["start_time"],
                            end_time=item["end_time"],
                        )
                        for item in response_json
                    ]
                else:
                    raise Exception(f"{response.status} Error: {await response.text()}")

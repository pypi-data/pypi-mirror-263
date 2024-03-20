import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod 
from datetime import datetime
import boto3

from opentldr import KnowledgeGraph
import opentldr.Domain as domain

load_dotenv()

import logging
logging.basicConfig(format='OpenTLDR Logging: %(message)s')
_log=logging.getLogger("OpenTLDR")

class AbstractContentRepo:
    kg:KnowledgeGraph=None

    @abstractmethod
    def importContentData(self) -> list[str]:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass

    def importTextContent(self,
                          kg:KnowledgeGraph,
                          text:str,
                          url:str,
                          default_source_name:str="unknown",
                          title:str="untitled",
                          date:datetime.date=datetime.now().date(),
                          type:str="news",
                          author:str="unknown") -> domain.Content:
            '''
            importTextContent processes the lines in a text block, extracts some metadata, and stores it as
            Content nodes in the KnowledgeGraph. This is used by the implementations of the abstract class
            AbstractContentRepo once they retrieve text content from their source. All of the metadata can be
            passed into this method, but will be overwritten by that discovered within the text (if any).
            '''
            content_text=""
            source=None
                    
            for line in text.splitlines():
                if line.startswith("date:"):
                    content_date = datetime.strptime(line.split(":",1)[1].strip(),'%m/%d/%Y').date()
                elif line.startswith("title:"):
                    title = line.split(":",1)[1].strip()
                elif line.startswith("url:"):
                    url = line.split(":",1)[1].strip()
                elif line.startswith("type:"):
                    type = line.split(":",1)[1].strip()
                elif line.startswith("source:"):
                    source_name = line.split(":",1)[1].strip()
                    source=kg.get_source_by_name(name=source_name)
                    if source is None: # Identified source not in KG so add it
                        source=kg.add_source(name=source_name)
                elif line.startswith("author:"):
                    author = line.split(":",1)[1].strip()
                else:
                    content_text=content_text.join(["\n",line])
                
            # write Content node to KG
            if source is None: # No source specified in file
                source=kg.get_source_by_name(name=default_source_name)
                if source is None: # Default does not exist in KG yet
                    source=kg.add_source(name=default_source_name)

            content=kg.add_content(source=source, type=type, url=url, date=date, title=title, text=content_text.strip())
            return content

    def importTextRequest(self,
                          kg:KnowledgeGraph,
                          text:str,
                          default_user_name:str="unknown",
                          default_user_email:str="unknown",
                          title:str="untitled",
                          date:datetime.date=datetime.now().date()) -> domain.Request:
            '''
            importTextRequest processes the lines in a text block, extracts some metadata, and stores it as
            Request nodes in the KnowledgeGraph. This is used by the implementations of the abstract class
            AbstractContentRepo once they retrieve text content from their source. All of the metadata can be
            passed into this method, but will be overwritten by that discovered within the text (if any).
            '''
            request_text=""
            user=None
                    
            for line in text.splitlines():
                if line.startswith("date:"):
                    request_date = datetime.strptime(line.split(":",1)[1].strip(),'%m/%d/%Y').date()
                elif line.startswith("title:"):
                    title = line.split(":",1)[1].strip()
                elif line.startswith("user:"):
                    user_name = line.split(":",1)[1].strip()
                    user=kg.get_user_by_name(name=user_name)
                    if user is None: # Identified source not in KG so add it
                        usr=kg.add_source(name=user_name)
                else:
                    content_text=content_text.join(["\n",line])
                
            # write Content node to KG
            if user is None: # No user specified in file
                user=kg.get_user_by_name(name=default_user_name)
                if user is None: # Default does not exist in KG yet
                    user=kg.add_user(name=default_user_name, email=default_user_email)

            request=kg.add_request(user=user, title=title, text=content_text.strip())
            return request

class TxtFileContentRepo(AbstractContentRepo):
    '''
    Reads all the text files in the provided directory path. Creates a Source node for the directory and parses the text files.
    This extracts lines with property definitions (e.g., "date: 05/14/1960 08:00PM") and puts the rest into the text body.
    Creates a Content node, for each file and adds it to the knowledge graph.
    '''
    ingest_path:str = "."

    def __init__(self, kg:KnowledgeGraph, ingest_path="."):
        self.kg=kg
        self.ingest_path = ingest_path

    def describe(self) -> str:
        return "Text File Content (path = '{path}')".format(path=self.ingest_path)

    def importContentData(self) -> list[str]:
        _log.info("Importing Content from File System...")
        default_source_name = "File System Directory:{path}".format(path=self.ingest_path)
        list_of_uids = []

        # read in each text file from directory
        for filename in os.listdir(self.ingest_path):

            # ignore anything but files that end in .txt
            if os.path.splitext(filename)[1] != ".txt" or not os.path.isfile(os.path.join(self.ingest_path, filename)):
                continue

            # do not reimport articles that are already in the KG
            #if kg.get_content_by_url(url=filename) is not None:
            #    _log.info("Skipping content already in KG: {url}".format(url=filename))
            #    continue

            full_path=os.path.join(self.ingest_path, filename)
            with open(full_path) as f:
                text = f.read()
                url="file://{path}".format(path=os.path.abspath(full_path))
                content=self.importTextContent(kg=self.kg, text=text, url=url, default_source_name=default_source_name)
                list_of_uids.append(content.uid)

        return list_of_uids

class S3ContentRepo(AbstractContentRepo):

    bucket = None
    bucket_name=""
   
    def __init__(self, kg:KnowledgeGraph, bucket_name:str, aws_access_key_id:str, aws_secret_access_key:str):
        self.kg=kg
        session = boto3.Session( aws_access_key_id, aws_secret_access_key)
        s3 = session.resource('s3')
        self.bucket_name=bucket_name
        self.bucket = s3.Bucket(bucket_name)

    def describe(self) -> str:
        return "S3 Bucket Content ('{bucket}')".format(bucket=self.bucket_name)

    def importContentData(self) -> list[str]:
        _log.info("Importing Content from S3 Bucket...")
        default_source_name = "S3 Bucket:{path}".format(path=self.bucket_name)
        list_of_uids = []

        # read in each text file from directory
        for object in self.bucket.objects.all():
            # ignore anything but files that end in .txt
            if not object.key.endswith('txt'):
                continue

            url="https://{bucket_name}.s3.amazonaws.com/{object_name}".format(bucket_name=self.bucket_name, object_name=object.key)
            text=object.get()['Body'].read().decode()
            content=self.importTextContent(kg=self.kg, text=text, url=url, default_source_name=default_source_name)
            list_of_uids.append(content.uid)

        return list_of_uids


class RssContentRepo(AbstractContentRepo):
    feedname:str="unknown"

    def describe(self) -> str:
        return "RSS Feed Content ('{feed}')".format(feed=self.feed_name)
    
    def importContentData(self) -> list[str]:
        _log.info("Importing Content from RSS Feed...")
        raise NotImplementedError("RSS Feed Content Repo is not yet implemented.")

class MongoContentRepo(AbstractContentRepo):
    collection:str="unknown"

    def describe(self) -> str:
        return "MongoDB Content ('{collection}')".format(collection=self.collection)

    def importContentData(self) -> list[str]:
        _log.info("Importing Content from MongoDB...")
        raise NotImplementedError("MongoDB Content Repo is not yet implemented.")

class ContentRepo(AbstractContentRepo):
    repo:AbstractContentRepo

    def _configOrEnv(self, key:str, config:dict) -> str:
        value:str=config.get(key)
        if value is None:
            value = config.get(key.capitalize())
        if value is None:
            value = os.getenv(key)
        if value is None:
            value = os.getenv(key.capitalize())
        if value is None:
            raise TypeError("No value found for '{key}', which is required.".format(key=key))
        return value

    def __init__(self, kg:KnowledgeGraph, config:dict):
        if config is None:
            _log.warn("No config file passed to ContentRepo, defaulting to using environment variables.")
            config="{}"

        type = self._configOrEnv("repo_type",config);
        if type is None or type not in ['s3','files']:
            message=("RepoFactor requires a dictionary structure as a parameter that includes at least a 'repo_type' entry set to one of 's3' or 'file'.")
            _log.error(message)
            raise TypeError(message)
        
        match type:
            case "s3":
                bucket_name=self._configOrEnv("bucket",config)
                aws_access_key_id=self._configOrEnv("aws_access_key_id",config)
                aws_secret_access_key=self._configOrEnv("aws_secret_access_key",config)
                self.repo= S3ContentRepo(kg,bucket_name=bucket_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
            case "files":
                ingest_path=self._configOrEnv("path",config)
                self.repo= TxtFileContentRepo(kg,ingest_path=ingest_path)
            case _:
                message:str = "Invalid 'type' config ('{type}').".format(type=type)
                _log.error(message)
                raise NotImplementedError(message)
        
    def importReferenceData(self) -> list[str]:
        message:str = "Importing Reference Data is not implemented yet."
        _log.error(message)
        raise NotImplementedError(message)

    def importRequestData(self) -> list[str]:
        message:str = "Importing Request Data is not implemented yet."
        _log.error(message)
        raise NotImplementedError(message)

    def importContentData(self) -> list[str]:
        if self.repo is None:
            _log.error("No to ContentRepo was configured.")
        _log.info("Importing Content from ContentRepo: {repo}.".format(repo=self.repo.describe()))
        return self.repo.importContentData()
    
    def importFeedbackData(self) -> list[str]:
        message:str = "Importing Feedback Data is not implemented yet."
        _log.error(message)
        raise NotImplementedError(message)

    def importEvaluationData(self) -> list[str]:
        message:str = "Importing Evaluation Data is not implemented yet."
        _log.error(message)
        raise NotImplementedError(message)

    def describe(self) -> str:
        if self.repo is None:
            _log.error("No to ContentRepo was configured.")
        return self.repo.describe()
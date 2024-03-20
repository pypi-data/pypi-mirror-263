import neomodel as nm
from neomodel.cardinality import One, ZeroOrOne, ZeroOrMore, OneOrMore

import logging
logging.basicConfig(format='OpenTLDR Logging: %(message)s')
_log=logging.getLogger("OpenTLDR")

class OpenTldrMeta():
    '''
    OpenTldrMeta is a mixin class that adds a unique id (uid) and JSON property (metadata)
    to a Node or Edge. This is used in every Edge and Node in OpenTLDR and provides an
    interface for PyDantic for data manipulation and JSON.
    '''
    uid=nm.UniqueIdProperty()
    metadata=nm.JSONProperty(default="{}")
    
    def to_text(self) -> str:
        '''
        to_text() returns a user readable string representing the values in the object.
        '''
        return "uid: {uid}".format(uid=self.uid)
    
class OpenTldrText():
    '''
    OpenTldrText is a mixin class that adds the properties of text and type (both are Strings)
    to any Node or Edge. This is used whenever the client stores text in the knowledge graph.
    '''
    text = nm.StringProperty(required=True)
    type = nm.StringProperty(required=True)

    def to_text(self) -> str:
        return "type: {type}\t text: {text}".format(type=self.type,text=self.text)

class CitableNode(nm.StructuredNode):
    '''
    CitableNode is a baseclass for any Node from which we extract entities (e.g., NER)
    and we need to refer back to the Node from where they were detected.
    '''
    pass

class Uncertain():
    '''
    Uncertain is a mixin class that adds a confidence value (0.0-1.0) to a Node or Edge.
    This is implemented to store the float value and generate description qualatiative
    text clauses for the ranges of this confidence value.
    '''
    confidence = nm.FloatProperty(default=1.0)
    def uncertainty_to_text(self) -> str:
        if self.confidence < 0.05:
            return "with almost no chance"
        if self.confidence >= 0.05 and self.confidence < 0.20:
            return "very unlikely"
        if self.confidence >= 0.2 and self.confidence < 0.45:
            return "unlikely"
        if self.confidence >= 0.45 and self.confidence < 0.55:
            return "with roughly even chance"
        if self.confidence >= 0.55 and self.confidence < 0.8:
            return "likely"
        if self.confidence >= 0.8 and self.confidence < 0.95:
            return "very likely"
        if self.confidence >= 0.55 and self.confidence < 1.0:
            return "with almost certainty"
        return "with certainty"

class Scored():
    '''
    Scored is a mixin class that adds a score value (0.0-1.0) to a Node or Edge.
    This is implemented to store the float value and generate descriptive qualatative
    text clauses for the ranges of this score value.
    '''
    score = nm.FloatProperty(default=1.0)
    def score_to_text(self) -> str:
        if self.score < 0.15:
            return "very low"
        if self.score >= 0.15 and self.score < 0.40:
            return "low"
        if self.score >= 0.4 and self.score < 0.6:
            return "medium"
        if self.score >= 0.6 and self.score < 0.85:
            return "high"
        if self.score >= 0.85 and self.score < 1.0:
            return "very high"
        return "perfect"

# Reference Knowledge

class ReferenceEdge(nm.StructuredRel, OpenTldrText, OpenTldrMeta):
    '''
    ReferenceEdge allows for general reference data relationships to be introduced into the 
    knowledge graph and used abstractly (e.g., ontological distance using path finding).
    This uses the OpenTldrText mixin to implement text and type properties.
    '''
    hypothesized = nm.BooleanProperty(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_hypothesized(self) -> bool:
        return self.hypothesized

    def set_hypothesized(self, is_hypothesized:bool):
        self.hypothesized=is_hypothesized

    def to_text(self) -> str:
        left:ReferenceNode = self.start_node()
        right:ReferenceNode = self.end_node()
        return "{left} -[{relationship}:{type}]-> {right}".format(left=left.text,
                                                           right=right.text,
                                                           relationship=self.text,
                                                           type=self.type)


class ReferenceNode(nm.StructuredNode, OpenTldrText, OpenTldrMeta):
    '''
    ReferenceNode allos for general reference data nodes to be introduced into the 
    knowledge graph and used abstractly (e.g., to relate extracted entities to known things).
    This uses the OpenTldrText mixin to implement text and type properties.
    The hypothesized property is a boolean that indicates if this was inferred (e.g., discovered)
    or provided as fact via external reference data (e.g., imported). 
    '''
    hypothesized = nm.BooleanProperty(default=False)
    edges = nm.RelationshipTo('ReferenceNode','REFERENCE_EDGE', model=ReferenceEdge, cardinality=ZeroOrMore)

    def is_hypothesized(self) -> bool:
        return self.hypothesized

    def set_hypothesized(self, is_hypothesized:bool):
        self.hypothesized=is_hypothesized

    def connect_to(self, to_node:'ReferenceNode') -> ReferenceEdge:
        return self.edges.connect(to_node)

    def to_text(self) -> str:
        return "'{text}' of type {type}".format(text=self.text,type=self.type)
    

# Active Data

class Source(nm.StructuredNode, OpenTldrMeta):
    '''
    Source nodes indicate the generator of various content. This may be an author or distributor
    of information. The name property is used to uniquely identify the source.
    '''
    name = nm.StringProperty(unique_index=True, required=True)

class IsFrom(nm.StructuredRel, OpenTldrMeta):
    '''
    IsFrom edges connect Content nodesM to the Source nodes in the knowledge graph.
    '''
    def to_text(self) -> str:
        return "The {content_type} '{content_title}' is from the source {end}.".format(
            content_type= self.start_node().type,
            content_title=self.start_node().title,
            end=self.end_node().name)
    
class Content(CitableNode, OpenTldrMeta, OpenTldrText):
    '''
    Content nodes represent text-based information, such as a news article or message.
    They include properties for title (String), date (datetime.date), and url (String).
    In OpenTldr Content node urls are used for hyperlinks back to the original material.
    '''
    title = nm.StringProperty(required=True)
    date = nm.properties.DateProperty(required=True)
    url = nm.StringProperty(required=True)
    is_from = nm.RelationshipTo(Source, 'IS_FROM', model=IsFrom, cardinality=One)
    
class MentionedIn(nm.StructuredRel, OpenTldrMeta):
    '''
    MentionedIn edges connects an extracted Entity node to the CitableNode (e.g., Content 
    or Request) that included the reference.
    '''
    def to_text(self) -> str:
        return "The entity '{entity}' is mentioned in the '{title}'.".format(
            entity=self.start_node().text,
            title=self.end_node().title)

class RefersTo(nm.StructuredRel, OpenTldrMeta, Uncertain):
    '''
    RefersTo edges connects an extracted Entity node to the ReferenceNode that is it believed
    to represent with the uncertainity value provided. 
    '''
    def to_text(self) -> str:
        return "The entity '{entity}' {uncertainty} refers to '{ref}'.".format(
            entity=self.start_node().text,
            ref=self.end_node().text,
            uncertainty=self.uncertainty_to_text())

class Entity(nm.StructuredNode, OpenTldrText, OpenTldrMeta):
    '''
    Entity nodes represent specific things that are "mentioned_in" in Citable nodes 
    (e.g., Content or Requests) that "refers_to" some ReferenceNode information. The text property
    contains the text for the entity identified and they type property expresses what it is.
    The "refers_to" edge can be uncertain (e.g., sematic similarity of text and type consistency). 
    '''
    refers_to=nm.RelationshipTo(ReferenceNode,'REFERS_TO', model = RefersTo, cardinality=ZeroOrMore)  
    mentioned_in = nm.RelationshipTo("CitableNode", 'MENTIONED_IN', model=MentionedIn, cardinality=OneOrMore)

# Information Request

class User(nm.StructuredNode, OpenTldrMeta):
    '''
    User node represents a client of the OpenTLDR system and has name and email properties (Stings).
    Similar to a Content connecting to a Source, Requests connect to a User (see RequestedBy edge).
    '''
    name = nm.StringProperty(required=True)
    email = nm.StringProperty(required=True)
    def to_text(self) -> str:
        return "The User '{name}' with email '{email}'.".format(
            name=self.name, email=self.email)

class RequestedBy(nm.StructuredRel, OpenTldrMeta):
    '''
    RequestedBy edges connect Request nodes to the User node to reflect who made the request.
    '''
    def to_text(self) -> str:
        return "The request '{request}' was requested by {user}.".format(
            request=self.start_node().title,
            user=self.end_node().name)

class Request(CitableNode, OpenTldrMeta):
    '''
    Request nodes information requests that are made by users to indicate what information they
    are interested in and how to tailor that information for them. A "text" property (String) 
    holds the text of the information request and the "title" property (String) provides a 
    short labels for the request to avoid repeating long request text. The "requested_by" edge
    links each request to one User node.
    '''
    title=nm.StringProperty(required=True)
    text = nm.StringProperty(required=True)
    requested_by = nm.RelationshipTo(User, 'REQUESTED_BY', model=RequestedBy, cardinality=One)

# Workflow Products / Recommendations and Summaries

class Recommends(nm.StructuredRel, OpenTldrMeta):
    '''
    Recommends edge connects a Recommendation node to the Content node that is being recommended.
    '''
    def to_text(self) -> str:
        return "This has {score} relevance for {content_type} '{content_title}'.".format(
            content_title=self.end_node().title,
            content_type= self.end_node().type,
            score=self.start_node.score_to_text())

class RelatesTo(nm.StructuredRel, OpenTldrMeta):
    '''
    RelatesTo edge connects a Recommendation node to the Request on which it is based.
    '''
    def to_text(self) -> str:
        return "This has {score} relevance to the request '{request}'.".format(
            request= self.end_node().title,
            score=self.start_node().score_to_text())

class Recommendation(nm.StructuredNode, OpenTldrMeta, Scored):
    '''
    Recommendation nodes represent the assertion that a Content node (pointed to by Recommends edge)
    is believed to be relevant to a Request node (pointed to by the RelatesTo edge). The score
    property (float 0.0 - 1.0) indicates how relevant and thus how strong the recommendation.
    '''
    recommends = nm.RelationshipTo(Content, 'RECOMMENDS', model=Recommends, cardinality=One)
    relates_to = nm.RelationshipTo(Request, 'RELATES_TO', model=RelatesTo, cardinality=One)
    def to_text(self) -> str:
        return "The {content_type} '{content_title}' has {score} relevance to the request '{request}'.".format(
            content_title=self.recommends.single().text,
            content_type= self.recommends.single().type,
            request= self.relates_to.single().title,
            score=self.score_to_text())

class Summarizes(nm.StructuredRel, OpenTldrMeta):
    '''
    Summerizes edges connect a Summary node to the Content node that they summarize.
    '''
    pass

class FocusOn(nm.StructuredRel, OpenTldrMeta, Uncertain):
    '''
    FocusOn edges connect a Summary node to the Recommendation node that may help inform what
    the most relevant parts of the Summary are with respect to that Recommendation / Request.
    '''
    pass

class Summary(nm.StructuredNode, OpenTldrMeta):
    '''
    Summary node contains text (String property) that is a shortened (ideally tailored) version
    of the Content node connect with the "summaries" edge. The "focus_on" edge connects to the
    Recommendation that may inform how this summary is tailored.
    '''
    text = nm.StringProperty(required=True)
    summarizes = nm.RelationshipTo(Content, 'SUMMARIZES', model=Summarizes, cardinality=One)
    focus_on = nm.RelationshipTo(Recommendation, 'FOCUS_ON', model=FocusOn, cardinality=ZeroOrOne)

# Workflow Products / TLDR related classes

class Includes(nm.StructuredRel, OpenTldrMeta):
    '''
    Includes edges connect a TldrEntry node to a Summary node to indicate that the Summary is
    to be used in that part of the TLDR.
    '''
    pass

class BasedOn(nm.StructuredRel, OpenTldrMeta):
    '''
    BasedOn edges connect a TldrEntry node to a Recommendation ndoe to indicate why that
    entry is being included in the TLDR and may be used for things like ordering the entries
    to show the most recommended first.
    '''
    pass

class TldrEntry(nm.StructuredNode, OpenTldrMeta):
    '''
    TldrEntry is one record within a TLDR. In general, there is a one-to-one relationship
    between each TldrEntry, Recommendation, and Summary such that each record within a TLDR
    has a score for the Recommendation, a text blurb from the Summary, and a connection back
    to the original Content (from both the Recommendation and Summary).
    '''
    link = nm.StringProperty(required=False)
    includes = nm.RelationshipTo(Summary, 'INCLUDES', model=Includes, cardinality=One)
    based_on = nm.RelationshipTo(Recommendation, 'BASED_ON', model=BasedOn, cardinality=One)
    def to_text(self) -> str:
        return "The entry '{entry}' summarizes {content_type} '{content_title}' and {score} relevance to the request '{request}'.".format(
            entry=self.includes.single().summarizes.single().title,
            content_title=self.includes.single().summarizes.single().title,
            content_type= self.includes.single().summarizes.single().type,
            request= self.based_on.single().relates_to.single().title,
            score=self.based_on.single().score_to_text())

class Priority(nm.StructuredRel, OpenTldrMeta, Scored):
    '''
    Entries edges connect a Tldr to each of the TldrEntry objects that is make it up. The assumption
    here is that the score property (float 0.0 - 1.0) on the edge provides a decending ordering for
    the entries connected by these links.
    '''
    pass

class ResponseTo(nm.StructuredRel, OpenTldrMeta):
    '''
    ResponseTo edges connect a Tldr to the Request for which is was generated.
    '''
    pass

class Tldr(nm.StructuredNode, OpenTldrMeta):
    '''
    Tldr nodes represent an instance of the TLDR report for the date (in 'date' property of type
    datetime.date). It is connected to the Request by the ResponseTo edge and a set of TldrEntries
    by "Entries" edges.
    '''
    date = nm.DateProperty(required=True)
    priority = nm.RelationshipTo(TldrEntry, 'PRIORITY', model=Priority, cardinality=ZeroOrMore)
    response_to = nm.RelationshipTo(Request, 'RESPONSE_TO', model=ResponseTo, cardinality=One)
    def to_text(self) -> str:
        out:str = "The TLDR for request '{request}' on date {date} includes: ".format(
            request= self.response_to.single().title,
            date=self.date)
        for tldr_entry in self.priority:
            out += "\t{text}\n".format(text=tldr_entry.to_text())
        return out

# USER FEEDBACK / RATING


class Rated(nm.StructuredRel, Scored):
    '''
    Rated edges connect a Request node to TldrEntry node to provide a method for applying a User
    Feedback score ("score" property is float with expected range of 0.0 - 1.0) to indicating
    how relevant that entry is with respect to the request. These edges are generally created
    by the UI when the user rates an entry (e.g., clicking on a star rating).
    '''
    date = nm.DateProperty(required=True)
    def to_text(self) -> str:
        return "The user {user} rated the entry {entry} as {score}.".format(
            user=self.start_node().name,
            entry=self.end_node().text,
            score=self.score_to_text())

# USER FEEDBACK / ACCESS 

class Accessed(nm.StructuredRel, Scored):
    '''
    Accessed edges connect a User node to a Content node to indicate that the user has made
    a request (via the UI) for the original content (i.e., the url). The date property indicates
    when the request was made.
    '''
    date = nm.DateProperty(required=True)
    def to_text(self) -> str:
        return "The user {user} accessed the content {title} on {date}.".format(
            user=self.start_node().name,
            title=self.end_node().title,
            date=self.date)

#import jsonpickle
#
#
#def to_jsonpickle(obj) -> str:
#    return jsonpickle.encode(obj)
#
#def from_jsonpickle(json_string):
#    return jsonpickle.decode(json_string)
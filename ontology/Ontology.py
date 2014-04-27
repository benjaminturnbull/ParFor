"""Unclassified. 
Auto generated. 
Ontology object.


There is weirdness here in that variables and classes are not capitalised
correctly. This is to keep in line with RDF standards. So for syntax 
purposes this seems correct in use, but looks terrible here. Pylint
really hates this file. 
"""


#import surf

class Ontology:
    
    nsDict = {}
    owl = None
    fs = None
    xsd = None
    comms = None
    rdfs = None
    comp = None
    fsdetail = None
    person = None
    rdf = None
    instance = None
    user = None
    base = None
    event = None
    metadata = None
    class owl:
        """ 
        owl
        auto generated
        """

        ns = None

        def __init__(self,name):
            self.ns = name


    class fs:
        """ 
        fs
        auto generated
        """

        ns = None
        Computer = None
        Disk = None
        Partition = None
        Directory = None
        File = None
        contains = None
        name = None
        path = None
        onFileSystem = None
        fileExtension = None
        permissions = None
        readPermissions = None
        writePermissions = None
        executionPermissions = None
        PermissionObject = None
        ownerPermission = None
        groupPermission = None
        otherPermission = None
        ownerAccount = None
        ownerGroup = None
        size = None
        mtime = None
        atime = None
        ctime = None
        inode = None

        def __init__(self,name):
            self.ns = name
            self.Computer = self.ns + "Computer"
            self.Disk = self.ns + "Disk"
            self.Partition = self.ns + "Partition"
            self.Directory = self.ns + "Directory"
            self.File = self.ns + "File"
            self.contains = self.ns + "contains"
            self.name = self.ns + "name"
            self.path = self.ns + "path"
            self.onFileSystem = self.ns + "onFileSystem"
            self.fileExtension = self.ns + "fileExtension"
            self.permissions = self.ns + "permissions"
            self.readPermissions = self.ns + "readPermissions"
            self.writePermissions = self.ns + "writePermissions"
            self.executionPermissions = self.ns + "executionPermissions"
            self.PermissionObject = self.ns + "PermissionObject"
            self.ownerPermission = self.ns + "ownerPermission"
            self.groupPermission = self.ns + "groupPermission"
            self.otherPermission = self.ns + "otherPermission"
            self.ownerAccount = self.ns + "ownerAccount"
            self.ownerGroup = self.ns + "ownerGroup"
            self.size = self.ns + "size"
            self.mtime = self.ns + "mtime"
            self.atime = self.ns + "atime"
            self.ctime = self.ns + "ctime"
            self.inode = self.ns + "inode"


    class xsd:
        """ 
        xsd
        auto generated
        """

        ns = None

        def __init__(self,name):
            self.ns = name


    class comms:
        """ 
        comms
        auto generated
        """

        ns = None
        Communication = None
        sendingProgram = None
        recievingProgram = None
        communication_topic = None
        communication_from = None
        communication_to = None
        communication_cc = None
        communication_bcc = None
        Communicates = None
        AsyncronouslyCommunicates = None
        SyncronouslyCommunicates = None
        Emails = None
        FacebookMessages = None
        MicrosoftCommunicatorMessages = None

        def __init__(self,name):
            self.ns = name
            self.Communication = self.ns + "Communication"
            self.sendingProgram = self.ns + "sendingProgram"
            self.recievingProgram = self.ns + "recievingProgram"
            self.communication_topic = self.ns + "communication_topic"
            self.communication_from = self.ns + "communication_from"
            self.communication_to = self.ns + "communication_to"
            self.communication_cc = self.ns + "communication_cc"
            self.communication_bcc = self.ns + "communication_bcc"
            self.Communicates = self.ns + "Communicates"
            self.AsyncronouslyCommunicates = self.ns + "AsyncronouslyCommunicates"
            self.SyncronouslyCommunicates = self.ns + "SyncronouslyCommunicates"
            self.Emails = self.ns + "Emails"
            self.FacebookMessages = self.ns + "FacebookMessages"
            self.MicrosoftCommunicatorMessages = self.ns + "MicrosoftCommunicatorMessages"


    class rdfs:
        """ 
        rdfs
        auto generated
        """

        ns = None
        Class = None
        comment = None
        label = None

        def __init__(self,name):
            self.ns = name
            self.Class = self.ns + "Class"
            self.comment = self.ns + "comment"
            self.label = self.ns + "label"


    class comp:
        """ 
        comp
        auto generated
        """

        ns = None
        Computer = None
        installedSoftware = None
        installedOperatingSystem = None
        Software = None
        OfficeSoftware = None
        CloudSoftware = None
        OperatingSystemSoftware = None

        def __init__(self,name):
            self.ns = name
            self.Computer = self.ns + "Computer"
            self.installedSoftware = self.ns + "installedSoftware"
            self.installedOperatingSystem = self.ns + "installedOperatingSystem"
            self.Software = self.ns + "Software"
            self.OfficeSoftware = self.ns + "OfficeSoftware"
            self.CloudSoftware = self.ns + "CloudSoftware"
            self.OperatingSystemSoftware = self.ns + "OperatingSystemSoftware"


    class fsdetail:
        """ 
        fsdetail
        auto generated
        """

        ns = None
        isInvisible = None
        FileType = None
        associatedWithExtension = None
        MediaFileType = None
        ImageFileType = None
        MovieFileType = None
        SystemFileType = None
        OfficeFileType = None
        CompoundFileType = None
        fileSpecificMetadata = None
        exifMetadata = None
        shotTimeMetadata = None
        shotLatitudeMetadata = None
        shotLongitudeMetadata = None

        def __init__(self,name):
            self.ns = name
            self.isInvisible = self.ns + "isInvisible"
            self.FileType = self.ns + "FileType"
            self.associatedWithExtension = self.ns + "associatedWithExtension"
            self.MediaFileType = self.ns + "MediaFileType"
            self.ImageFileType = self.ns + "ImageFileType"
            self.MovieFileType = self.ns + "MovieFileType"
            self.SystemFileType = self.ns + "SystemFileType"
            self.OfficeFileType = self.ns + "OfficeFileType"
            self.CompoundFileType = self.ns + "CompoundFileType"
            self.fileSpecificMetadata = self.ns + "fileSpecificMetadata"
            self.exifMetadata = self.ns + "exifMetadata"
            self.shotTimeMetadata = self.ns + "shotTimeMetadata"
            self.shotLatitudeMetadata = self.ns + "shotLatitudeMetadata"
            self.shotLongitudeMetadata = self.ns + "shotLongitudeMetadata"


    class person:
        """ 
        person
        auto generated
        """

        ns = None
        Person = None
        givenName = None
        middle1Name = None
        middle2Name = None
        middle3Name = None
        middle4Name = None
        familyName = None
        personLinkedToComputer = None
        personAccessesComputer = None
        personOwnsComputer = None
        personLinkedToAccount = None
        accountLinkedToPerson = None

        def __init__(self,name):
            self.ns = name
            self.Person = self.ns + "Person"
            self.givenName = self.ns + "givenName"
            self.middle1Name = self.ns + "middle1Name"
            self.middle2Name = self.ns + "middle2Name"
            self.middle3Name = self.ns + "middle3Name"
            self.middle4Name = self.ns + "middle4Name"
            self.familyName = self.ns + "familyName"
            self.personLinkedToComputer = self.ns + "personLinkedToComputer"
            self.personAccessesComputer = self.ns + "personAccessesComputer"
            self.personOwnsComputer = self.ns + "personOwnsComputer"
            self.personLinkedToAccount = self.ns + "personLinkedToAccount"
            self.accountLinkedToPerson = self.ns + "accountLinkedToPerson"


    class rdf:
        """ 
        rdf
        auto generated
        """

        ns = None
        type = None
        Property = None
        Class = None

        def __init__(self,name):
            self.ns = name
            self.type = self.ns + "type"
            self.Property = self.ns + "Property"
            self.Class = self.ns + "Class"


    class instance:
        """ 
        instance
        auto generated
        """

        ns = None

        def __init__(self,name):
            self.ns = name


    class user:
        """ 
        user
        auto generated
        """

        ns = None
        UserAccount = None
        UserGroup = None
        groupName = None
        groupId = None
        groupContainsUser = None
        userContainedWithinGroup = None

        def __init__(self,name):
            self.ns = name
            self.UserAccount = self.ns + "UserAccount"
            self.UserGroup = self.ns + "UserGroup"
            self.groupName = self.ns + "groupName"
            self.groupId = self.ns + "groupId"
            self.groupContainsUser = self.ns + "groupContainsUser"
            self.userContainedWithinGroup = self.ns + "userContainedWithinGroup"


    class base:
        """ 
        base
        auto generated
        """

        ns = None
        metadataProperty = None
        hashType = None
        md5HashType = None
        sha256HashType = None
        passwordHashType = None
        ntPasswordHashType = None
        ntlmPasswordHashType = None
        name = None
        mountPoint = None
        username = None
        userId = None
        homeDirectory = None
        passwordHash = None

        def __init__(self,name):
            self.ns = name
            self.metadataProperty = self.ns + "metadataProperty"
            self.hashType = self.ns + "hashType"
            self.md5HashType = self.ns + "md5HashType"
            self.sha256HashType = self.ns + "sha256HashType"
            self.passwordHashType = self.ns + "passwordHashType"
            self.ntPasswordHashType = self.ns + "ntPasswordHashType"
            self.ntlmPasswordHashType = self.ns + "ntlmPasswordHashType"
            self.name = self.ns + "name"
            self.mountPoint = self.ns + "mountPoint"
            self.username = self.ns + "username"
            self.userId = self.ns + "userId"
            self.homeDirectory = self.ns + "homeDirectory"
            self.passwordHash = self.ns + "passwordHash"


    class event:
        """ 
        event
        auto generated
        """

        ns = None
        Event = None
        actor = None
        verb = None
        theme = None
        instrument = None
        Verb = None
        ComputerStateChangeVerb = None
        ComputerPoweredOn = None
        ComputerPoweredOff = None
        ComputerHibernateOn = None
        ComputerHibernateOff = None
        UserLoginEventVerb = None
        UserLogIn = None
        UserLogOut = None

        def __init__(self,name):
            self.ns = name
            self.Event = self.ns + "Event"
            self.actor = self.ns + "actor"
            self.verb = self.ns + "verb"
            self.theme = self.ns + "theme"
            self.instrument = self.ns + "instrument"
            self.Verb = self.ns + "Verb"
            self.ComputerStateChangeVerb = self.ns + "ComputerStateChangeVerb"
            self.ComputerPoweredOn = self.ns + "ComputerPoweredOn"
            self.ComputerPoweredOff = self.ns + "ComputerPoweredOff"
            self.ComputerHibernateOn = self.ns + "ComputerHibernateOn"
            self.ComputerHibernateOff = self.ns + "ComputerHibernateOff"
            self.UserLoginEventVerb = self.ns + "UserLoginEventVerb"
            self.UserLogIn = self.ns + "UserLogIn"
            self.UserLogOut = self.ns + "UserLogOut"


    class metadata:
        """ 
        metadata
        auto generated
        """

        ns = None
        Reasoner = None

        def __init__(self,name):
            self.ns = name
            self.Reasoner = self.ns + "Reasoner"


    def __init__(self):

        """
        Initialisation
        """
        
        self.owl = Ontology.owl ('http://www.w3.org/2002/07/owl#')
        self.nsDict["owl"] = "http://www.w3.org/2002/07/owl#"
        self.fs = Ontology.fs ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/fs#')
        self.nsDict["fs"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/fs#"
        self.xsd = Ontology.xsd ('http://www.w3.org/2001/XMLSchema#')
        self.nsDict["xsd"] = "http://www.w3.org/2001/XMLSchema#"
        self.comms = Ontology.comms ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/comms#')
        self.nsDict["comms"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/comms#"
        self.rdfs = Ontology.rdfs ('http://www.w3.org/2000/01/rdf-schema#')
        self.nsDict["rdfs"] = "http://www.w3.org/2000/01/rdf-schema#"
        self.comp = Ontology.comp ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/comp#')
        self.nsDict["comp"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/comp#"
        self.fsdetail = Ontology.fsdetail ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/fsdetail#')
        self.nsDict["fsdetail"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/fsdetail#"
        self.person = Ontology.person ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/person#')
        self.nsDict["person"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/person#"
        self.rdf = Ontology.rdf ('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        self.nsDict["rdf"] = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        self.instance = Ontology.instance ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/instance#')
        self.nsDict["instance"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/instance#"
        self.user = Ontology.user ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/user#')
        self.nsDict["user"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/user#"
        self.base = Ontology.base ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/base#')
        self.nsDict["base"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/base#"
        self.event = Ontology.event ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/event#')
        self.nsDict["event"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/event#"
        self.metadata = Ontology.metadata ('http://pax.dsto.defence.gov.au/ParFor/2012-12-10/metadata#')
        self.nsDict["metadata"] = "http://pax.dsto.defence.gov.au/ParFor/2012-12-10/metadata#"

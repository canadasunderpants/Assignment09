#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
# jdenhaan, 2022-Dec-11, added methods to return track data for use in display and saving to file, 
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        tr_position: (int) with Track position on CD / Album
        tr_title: (str) with Track title
        tr_length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    # TODO add Track class code
    # -- Constructor -- #
    def __init__(self, tr_position: int, tr_title: str, tr_length: str) -> None:
        """ set position, title, and leght of new Track object"""
        # -- Attributes -- #
        try:
            self.__tr_position = int(tr_position)
            self.__tr_title = str(tr_title)
            self.__tr_length = str(tr_length)
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))
    # -- Properties -- #
    # Track position
    @property
    def tr_position(self):
        return self.__tr_position

    @tr_position.setter
    def tr_position(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('position needs to be Integer')
    # Track title
    @property
    def tr_title(self):
        return self.__tr_title

    @tr_title.setter
    def tr_title(self, value):
        try:
            self.__tr_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')
    # Track Length
    @property
    def tr_length(self):
        return self.__tr_length

    @tr_length.setter
    def tr_length(self, value):
        try:
            self.__tr_length = str(value)
        except Exception:
            raise Exception('length needs to be String!')

    # -- Methods -- #
    # TODO Add Track class methods
    def __str__(self):
        """Returns Track details as formatted string"""
        return '{:>2}\t{} (length: {})'.format(self.tr_position, self.tr_title, self.tr_length)

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(self.tr_position, self.tr_title, self.tr_length)


class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

    """
    # TODONE Modify CD class as required
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str, cd_tracks = []) -> None:
        """Set ID, Title and Artist of a new CD Object. Tracks is a list type whose default value
        is None to account for new albums that may not have tracks added yet. """
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__cd_tracks = []
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__cd_tracks

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        # TODONE append track
        self.__cd_tracks.append(track)
        # TODONE sort tracks
        self.__sort_tracks()

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """
        # TODONE remove track
        try:
            track_id = int(track_id)
        except:
            Exception ('Track ID is not an integer')
        del self.__cd_tracks[track_id - 1]
        self.__sort_tracks()
        # TODONE sort tracks

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__cd_tracks)
        for track in self.__cd_tracks:
            if (track is not None) and (n < track.tr_position):
                n = track.tr_position
        tmp_tracks = [None] * n
        for track in self.__cd_tracks:
            if track is not None:
                tmp_tracks[track.tr_position - 1] = track
        self.__cd_tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__cd_tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__cd_tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result





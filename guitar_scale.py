from typing import List, Optional

class GuitarScale:
    def __init__(self, key: str, scale_type: str):
        # The base list of chromatic notes
        self.notes: List[str] = [
            'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
        ]
        if key not in self.notes:
            raise ValueError(f"Invalid key '{key}'. Must be one of the notes: {self.notes}")

        self.key: str = key
        self.scale_type: str = scale_type
        self.blue_note: Optional[str] = None

        self.scale_notes: List[str] = self.generate_scale()

    def _search_in_notes(self, pattern: List[int]) -> List[str]:
        """
        Helper method to generate the note sequence based on an interval pattern.
        """
        start_index: int = self.notes.index(self.key)
        scale: List[str] = []
        for step in pattern:
            scale.append(self.notes[start_index])
            start_index = (start_index + step) % len(self.notes)
        return scale

    def major_scale(self) -> List[str]:
        """
        Generates the notes of the major scale.
        """
        pattern: List[int] = [2, 2, 1, 2, 2, 2, 1]
        return self._search_in_notes(pattern)

    def minor_scale(self) -> List[str]:
        """
        Generates the notes of the natural minor scale.
        """
        pattern: List[int] = [2, 1, 2, 2, 1, 2, 2]
        return self._search_in_notes(pattern)

    def pentatonic_major_scale(self) -> List[str]:
        """
        Generates the notes of the major pentatonic scale.
        """
        pattern: List[int] = [2, 2, 3, 2, 3]
        return self._search_in_notes(pattern)

    def pentatonic_minor_scale(self) -> List[str]:
        """
        Generates the notes of the minor pentatonic scale.
        """
        pattern: List[int] = [3, 2, 2, 3, 2]
        return self._search_in_notes(pattern)

    def blues_scale(self) -> List[str]:
        """
        Generates the notes of the blues scale (minor pentatonic + blue note).
        """
        pentatonic: List[str] = self.pentatonic_minor_scale()

        start_index: int = self.notes.index(self.key)
        self.blue_note = self.notes[(start_index + 6) % len(self.notes)]

        pentatonic.insert(3, self.blue_note)
        return pentatonic

    def generate_scale(self) -> List[str]:
        """
        Main method that decides which scale to generate based on the specified type.
        """
        match self.scale_type:
            case 'major':
                return self.major_scale()
            case 'minor':
                return self.minor_scale()
            case 'pentatonic_major':
                return self.pentatonic_major_scale()
            case 'pentatonic_minor':
                return self.pentatonic_minor_scale()
            case 'blues':
                return self.blues_scale()
            case _:
                # More detailed error message
                raise ValueError(f"Unknown scale type '{self.scale_type}'. Valid types: 'major', 'minor', 'pentatonic_major', 'pentatonic_minor', 'blues'.")


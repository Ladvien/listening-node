:py:mod:`listening_tool.transcription`
========================================

.. py:module:: listening_tool.transcription

.. autodoc2-docstring:: listening_tool.transcription
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Word <listening_tool.transcription.Word>`
     - .. autodoc2-docstring:: listening_tool.transcription.Word
          :summary:
   * - :py:obj:`Segment <listening_tool.transcription.Segment>`
     - .. autodoc2-docstring:: listening_tool.transcription.Segment
          :summary:
   * - :py:obj:`TranscriptionResult <listening_tool.transcription.TranscriptionResult>`
     - .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult
          :summary:
   * - :py:obj:`TranscribeConfig <listening_tool.transcription.TranscribeConfig>`
     - .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PHRASES_TO_IGNORE <listening_tool.transcription.PHRASES_TO_IGNORE>`
     - .. autodoc2-docstring:: listening_tool.transcription.PHRASES_TO_IGNORE
          :summary:

API
~~~

.. py:data:: PHRASES_TO_IGNORE
   :canonical: listening_tool.transcription.PHRASES_TO_IGNORE
   :value: ['', 'urn.com urn.schemas-microsoft-com.h']

   .. autodoc2-docstring:: listening_tool.transcription.PHRASES_TO_IGNORE

.. py:class:: Word
   :canonical: listening_tool.transcription.Word

   .. autodoc2-docstring:: listening_tool.transcription.Word

   .. py:attribute:: word
      :canonical: listening_tool.transcription.Word.word
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Word.word

   .. py:attribute:: start
      :canonical: listening_tool.transcription.Word.start
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Word.start

   .. py:attribute:: end
      :canonical: listening_tool.transcription.Word.end
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Word.end

   .. py:attribute:: probability
      :canonical: listening_tool.transcription.Word.probability
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Word.probability

   .. py:method:: load(data)
      :canonical: listening_tool.transcription.Word.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.transcription.Word.load

   .. py:method:: to_dict()
      :canonical: listening_tool.transcription.Word.to_dict

      .. autodoc2-docstring:: listening_tool.transcription.Word.to_dict

.. py:class:: Segment
   :canonical: listening_tool.transcription.Segment

   .. autodoc2-docstring:: listening_tool.transcription.Segment

   .. py:attribute:: id
      :canonical: listening_tool.transcription.Segment.id
      :type: int
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.id

   .. py:attribute:: seek
      :canonical: listening_tool.transcription.Segment.seek
      :type: int
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.seek

   .. py:attribute:: start
      :canonical: listening_tool.transcription.Segment.start
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.start

   .. py:attribute:: end
      :canonical: listening_tool.transcription.Segment.end
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.end

   .. py:attribute:: text
      :canonical: listening_tool.transcription.Segment.text
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.text

   .. py:attribute:: tokens
      :canonical: listening_tool.transcription.Segment.tokens
      :type: typing.List[int]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.tokens

   .. py:attribute:: temperature
      :canonical: listening_tool.transcription.Segment.temperature
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.temperature

   .. py:attribute:: avg_logprob
      :canonical: listening_tool.transcription.Segment.avg_logprob
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.avg_logprob

   .. py:attribute:: compression_ratio
      :canonical: listening_tool.transcription.Segment.compression_ratio
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.compression_ratio

   .. py:attribute:: no_speech_prob
      :canonical: listening_tool.transcription.Segment.no_speech_prob
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.no_speech_prob

   .. py:attribute:: words
      :canonical: listening_tool.transcription.Segment.words
      :type: typing.List[listening_tool.transcription.Word]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.Segment.words

   .. py:method:: __post_init__()
      :canonical: listening_tool.transcription.Segment.__post_init__

      .. autodoc2-docstring:: listening_tool.transcription.Segment.__post_init__

   .. py:method:: load(data)
      :canonical: listening_tool.transcription.Segment.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.transcription.Segment.load

   .. py:method:: to_dict()
      :canonical: listening_tool.transcription.Segment.to_dict

      .. autodoc2-docstring:: listening_tool.transcription.Segment.to_dict

.. py:class:: TranscriptionResult
   :canonical: listening_tool.transcription.TranscriptionResult

   .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult

   .. py:attribute:: text
      :canonical: listening_tool.transcription.TranscriptionResult.text
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.text

   .. py:attribute:: segments
      :canonical: listening_tool.transcription.TranscriptionResult.segments
      :type: list[listening_tool.transcription.Segment]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.segments

   .. py:attribute:: language
      :canonical: listening_tool.transcription.TranscriptionResult.language
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.language

   .. py:attribute:: processing_secs
      :canonical: listening_tool.transcription.TranscriptionResult.processing_secs
      :type: int
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.processing_secs

   .. py:attribute:: local_starttime
      :canonical: listening_tool.transcription.TranscriptionResult.local_starttime
      :type: datetime.datetime
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.local_starttime

   .. py:attribute:: processing_rolling_avg_secs
      :canonical: listening_tool.transcription.TranscriptionResult.processing_rolling_avg_secs
      :type: float
      :value: 0

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.processing_rolling_avg_secs

   .. py:method:: __post_init__()
      :canonical: listening_tool.transcription.TranscriptionResult.__post_init__

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.__post_init__

   .. py:method:: load(data)
      :canonical: listening_tool.transcription.TranscriptionResult.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.load

   .. py:method:: to_dict()
      :canonical: listening_tool.transcription.TranscriptionResult.to_dict

      .. autodoc2-docstring:: listening_tool.transcription.TranscriptionResult.to_dict

.. py:class:: TranscribeConfig
   :canonical: listening_tool.transcription.TranscribeConfig

   .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig

   .. py:attribute:: model
      :canonical: listening_tool.transcription.TranscribeConfig.model
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.model

   .. py:attribute:: device
      :canonical: listening_tool.transcription.TranscribeConfig.device
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.device

   .. py:attribute:: verbose
      :canonical: listening_tool.transcription.TranscribeConfig.verbose
      :type: bool | None
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.verbose

   .. py:attribute:: temperature
      :canonical: listening_tool.transcription.TranscribeConfig.temperature
      :type: typing.Union[float, typing.Tuple[float, ...]]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.temperature

   .. py:attribute:: compression_ratio_threshold
      :canonical: listening_tool.transcription.TranscribeConfig.compression_ratio_threshold
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.compression_ratio_threshold

   .. py:attribute:: logprob_threshold
      :canonical: listening_tool.transcription.TranscribeConfig.logprob_threshold
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.logprob_threshold

   .. py:attribute:: no_speech_threshold
      :canonical: listening_tool.transcription.TranscribeConfig.no_speech_threshold
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.no_speech_threshold

   .. py:attribute:: condition_on_previous_text
      :canonical: listening_tool.transcription.TranscribeConfig.condition_on_previous_text
      :type: bool
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.condition_on_previous_text

   .. py:attribute:: word_timestamps
      :canonical: listening_tool.transcription.TranscribeConfig.word_timestamps
      :type: bool
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.word_timestamps

   .. py:attribute:: prepend_punctuations
      :canonical: listening_tool.transcription.TranscribeConfig.prepend_punctuations
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.prepend_punctuations

   .. py:attribute:: append_punctuations
      :canonical: listening_tool.transcription.TranscribeConfig.append_punctuations
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.append_punctuations

   .. py:attribute:: initial_prompt
      :canonical: listening_tool.transcription.TranscribeConfig.initial_prompt
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.initial_prompt

   .. py:attribute:: clip_timestamps
      :canonical: listening_tool.transcription.TranscribeConfig.clip_timestamps
      :type: typing.Union[str, typing.List[float]]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.clip_timestamps

   .. py:attribute:: hallucination_silence_threshold
      :canonical: listening_tool.transcription.TranscribeConfig.hallucination_silence_threshold
      :type: typing.Optional[float]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.hallucination_silence_threshold

   .. py:attribute:: phrases_to_ignore
      :canonical: listening_tool.transcription.TranscribeConfig.phrases_to_ignore
      :type: list[str]
      :value: None

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.phrases_to_ignore

   .. py:method:: load(data)
      :canonical: listening_tool.transcription.TranscribeConfig.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.load

   .. py:method:: __post_init__()
      :canonical: listening_tool.transcription.TranscribeConfig.__post_init__

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.__post_init__

   .. py:method:: to_dict()
      :canonical: listening_tool.transcription.TranscribeConfig.to_dict

      .. autodoc2-docstring:: listening_tool.transcription.TranscribeConfig.to_dict

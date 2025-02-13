:py:mod:`listening_node.listening_node`
=======================================

.. py:module:: listening_node.listening_node

.. autodoc2-docstring:: listening_node.listening_node
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ListeningNode <listening_node.listening_node.ListeningNode>`
     - .. autodoc2-docstring:: listening_node.listening_node.ListeningNode
          :summary:

API
~~~

.. py:class:: ListeningNode(config: listening_node.config.ListeningNodeConfig, recording_device: listening_node.recording_device.RecordingDevice)
   :canonical: listening_node.listening_node.ListeningNode

   .. autodoc2-docstring:: listening_node.listening_node.ListeningNode

   .. rubric:: Initialization

   .. autodoc2-docstring:: listening_node.listening_node.ListeningNode.__init__

   .. py:method:: transcribe(audio_np: numpy.ndarray) -> listening_node.transcription.TranscriptionResult
      :canonical: listening_node.listening_node.ListeningNode.transcribe

      .. autodoc2-docstring:: listening_node.listening_node.ListeningNode.transcribe

   .. py:method:: listen(callback: typing.Optional[typing.Callable[[str, typing.Dict], None]] = None) -> None
      :canonical: listening_node.listening_node.ListeningNode.listen

      .. autodoc2-docstring:: listening_node.listening_node.ListeningNode.listen

   .. py:method:: _phrase_complete(phrase_time: datetime.datetime, now: datetime.datetime) -> bool
      :canonical: listening_node.listening_node.ListeningNode._phrase_complete

      .. autodoc2-docstring:: listening_node.listening_node.ListeningNode._phrase_complete

   .. py:method:: _deep_convert_np_float_to_float(data: dict) -> dict
      :canonical: listening_node.listening_node.ListeningNode._deep_convert_np_float_to_float

      .. autodoc2-docstring:: listening_node.listening_node.ListeningNode._deep_convert_np_float_to_float

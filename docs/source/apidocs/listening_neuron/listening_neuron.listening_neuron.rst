:py:mod:`listening_tool.listening_tool`
===========================================

.. py:module:: listening_tool.listening_tool

.. autodoc2-docstring:: listening_tool.listening_tool
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ListeningTool <listening_tool.listening_tool.ListeningTool>`
     - .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool
          :summary:

API
~~~

.. py:class:: ListeningTool(config: listening_tool.config.ListeningToolConfig, recording_device: listening_tool.recording_device.RecordingDevice)
   :canonical: listening_tool.listening_tool.ListeningTool

   .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool

   .. rubric:: Initialization

   .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool.__init__

   .. py:method:: transcribe(audio_np: numpy.ndarray) -> listening_tool.transcription.TranscriptionResult
      :canonical: listening_tool.listening_tool.ListeningTool.transcribe

      .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool.transcribe

   .. py:method:: listen(callback: typing.Optional[typing.Callable[[str, typing.Dict], None]] = None) -> None
      :canonical: listening_tool.listening_tool.ListeningTool.listen

      .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool.listen

   .. py:method:: _phrase_complete(phrase_time: datetime.datetime, now: datetime.datetime) -> bool
      :canonical: listening_tool.listening_tool.ListeningTool._phrase_complete

      .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool._phrase_complete

   .. py:method:: _deep_convert_np_float_to_float(data: dict) -> dict
      :canonical: listening_tool.listening_tool.ListeningTool._deep_convert_np_float_to_float

      .. autodoc2-docstring:: listening_tool.listening_tool.ListeningTool._deep_convert_np_float_to_float

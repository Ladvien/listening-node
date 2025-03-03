:py:mod:`listening_tool.config`
=================================

.. py:module:: listening_tool.config

.. autodoc2-docstring:: listening_tool.config
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ListeningToolConfig <listening_tool.config.ListeningToolConfig>`
     - .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig
          :summary:
   * - :py:obj:`Config <listening_tool.config.Config>`
     - .. autodoc2-docstring:: listening_tool.config.Config
          :summary:

API
~~~

.. py:class:: ListeningToolConfig
   :canonical: listening_tool.config.ListeningToolConfig

   .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig

   .. py:attribute:: record_timeout
      :canonical: listening_tool.config.ListeningToolConfig.record_timeout
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.record_timeout

   .. py:attribute:: phrase_timeout
      :canonical: listening_tool.config.ListeningToolConfig.phrase_timeout
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.phrase_timeout

   .. py:attribute:: in_memory
      :canonical: listening_tool.config.ListeningToolConfig.in_memory
      :type: bool
      :value: None

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.in_memory

   .. py:attribute:: log
      :canonical: listening_tool.config.ListeningToolConfig.log
      :type: bool
      :value: None

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.log

   .. py:attribute:: transcribe_config
      :canonical: listening_tool.config.ListeningToolConfig.transcribe_config
      :type: listening_tool.transcription.TranscribeConfig
      :value: None

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.transcribe_config

   .. py:method:: load(data)
      :canonical: listening_tool.config.ListeningToolConfig.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.load

   .. py:method:: __post_init__()
      :canonical: listening_tool.config.ListeningToolConfig.__post_init__

      .. autodoc2-docstring:: listening_tool.config.ListeningToolConfig.__post_init__

.. py:class:: Config
   :canonical: listening_tool.config.Config

   .. autodoc2-docstring:: listening_tool.config.Config

   .. py:attribute:: listening_tool
      :canonical: listening_tool.config.Config.listening_tool
      :type: listening_tool.config.ListeningToolConfig
      :value: None

      .. autodoc2-docstring:: listening_tool.config.Config.listening_tool

   .. py:attribute:: mic_config
      :canonical: listening_tool.config.Config.mic_config
      :type: listening_tool.mic.MicConfig
      :value: None

      .. autodoc2-docstring:: listening_tool.config.Config.mic_config

   .. py:attribute:: logging_config
      :canonical: listening_tool.config.Config.logging_config
      :type: listening_tool.logging_config.LoggingConfig | None
      :value: None

      .. autodoc2-docstring:: listening_tool.config.Config.logging_config

   .. py:method:: load(path)
      :canonical: listening_tool.config.Config.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.config.Config.load

   .. py:method:: __post_init__()
      :canonical: listening_tool.config.Config.__post_init__

      .. autodoc2-docstring:: listening_tool.config.Config.__post_init__

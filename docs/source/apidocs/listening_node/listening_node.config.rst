:py:mod:`listening_node.config`
===============================

.. py:module:: listening_node.config

.. autodoc2-docstring:: listening_node.config
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ListeningNodeConfig <listening_node.config.ListeningNodeConfig>`
     - .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig
          :summary:
   * - :py:obj:`Config <listening_node.config.Config>`
     - .. autodoc2-docstring:: listening_node.config.Config
          :summary:

API
~~~

.. py:class:: ListeningNodeConfig
   :canonical: listening_node.config.ListeningNodeConfig

   .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig

   .. py:attribute:: record_timeout
      :canonical: listening_node.config.ListeningNodeConfig.record_timeout
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.record_timeout

   .. py:attribute:: phrase_timeout
      :canonical: listening_node.config.ListeningNodeConfig.phrase_timeout
      :type: float
      :value: None

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.phrase_timeout

   .. py:attribute:: in_memory
      :canonical: listening_node.config.ListeningNodeConfig.in_memory
      :type: bool
      :value: None

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.in_memory

   .. py:attribute:: log
      :canonical: listening_node.config.ListeningNodeConfig.log
      :type: bool
      :value: None

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.log

   .. py:attribute:: transcribe_config
      :canonical: listening_node.config.ListeningNodeConfig.transcribe_config
      :type: listening_node.transcription.TranscribeConfig
      :value: None

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.transcribe_config

   .. py:method:: load(data)
      :canonical: listening_node.config.ListeningNodeConfig.load
      :classmethod:

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.load

   .. py:method:: __post_init__()
      :canonical: listening_node.config.ListeningNodeConfig.__post_init__

      .. autodoc2-docstring:: listening_node.config.ListeningNodeConfig.__post_init__

.. py:class:: Config
   :canonical: listening_node.config.Config

   .. autodoc2-docstring:: listening_node.config.Config

   .. py:attribute:: listening_node
      :canonical: listening_node.config.Config.listening_node
      :type: listening_node.config.ListeningNodeConfig
      :value: None

      .. autodoc2-docstring:: listening_node.config.Config.listening_node

   .. py:attribute:: mic_config
      :canonical: listening_node.config.Config.mic_config
      :type: listening_node.mic.MicConfig
      :value: None

      .. autodoc2-docstring:: listening_node.config.Config.mic_config

   .. py:attribute:: logging_config
      :canonical: listening_node.config.Config.logging_config
      :type: listening_node.logging_config.LoggingConfig | None
      :value: None

      .. autodoc2-docstring:: listening_node.config.Config.logging_config

   .. py:method:: load(path)
      :canonical: listening_node.config.Config.load
      :classmethod:

      .. autodoc2-docstring:: listening_node.config.Config.load

   .. py:method:: __post_init__()
      :canonical: listening_node.config.Config.__post_init__

      .. autodoc2-docstring:: listening_node.config.Config.__post_init__

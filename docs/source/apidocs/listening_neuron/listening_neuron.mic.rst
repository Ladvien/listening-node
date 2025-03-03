:py:mod:`listening_tool.mic`
==============================

.. py:module:: listening_tool.mic

.. autodoc2-docstring:: listening_tool.mic
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`MicConfig <listening_tool.mic.MicConfig>`
     - .. autodoc2-docstring:: listening_tool.mic.MicConfig
          :summary:
   * - :py:obj:`Mic <listening_tool.mic.Mic>`
     - .. autodoc2-docstring:: listening_tool.mic.Mic
          :summary:

API
~~~

.. py:class:: MicConfig
   :canonical: listening_tool.mic.MicConfig

   .. autodoc2-docstring:: listening_tool.mic.MicConfig

   .. py:attribute:: mic_name
      :canonical: listening_tool.mic.MicConfig.mic_name
      :type: str
      :value: None

      .. autodoc2-docstring:: listening_tool.mic.MicConfig.mic_name

   .. py:attribute:: sample_rate
      :canonical: listening_tool.mic.MicConfig.sample_rate
      :type: int
      :value: None

      .. autodoc2-docstring:: listening_tool.mic.MicConfig.sample_rate

   .. py:attribute:: energy_threshold
      :canonical: listening_tool.mic.MicConfig.energy_threshold
      :type: int
      :value: None

      .. autodoc2-docstring:: listening_tool.mic.MicConfig.energy_threshold

   .. py:method:: load(data)
      :canonical: listening_tool.mic.MicConfig.load
      :classmethod:

      .. autodoc2-docstring:: listening_tool.mic.MicConfig.load

.. py:class:: Mic
   :canonical: listening_tool.mic.Mic

   .. autodoc2-docstring:: listening_tool.mic.Mic

   .. py:attribute:: config
      :canonical: listening_tool.mic.Mic.config
      :type: listening_tool.mic.MicConfig
      :value: None

      .. autodoc2-docstring:: listening_tool.mic.Mic.config

   .. py:attribute:: source
      :canonical: listening_tool.mic.Mic.source
      :type: speech_recognition.Microphone | None
      :value: None

      .. autodoc2-docstring:: listening_tool.mic.Mic.source

   .. py:method:: __post_init__()
      :canonical: listening_tool.mic.Mic.__post_init__

      .. autodoc2-docstring:: listening_tool.mic.Mic.__post_init__

   .. py:method:: _handle_linux()
      :canonical: listening_tool.mic.Mic._handle_linux

      .. autodoc2-docstring:: listening_tool.mic.Mic._handle_linux

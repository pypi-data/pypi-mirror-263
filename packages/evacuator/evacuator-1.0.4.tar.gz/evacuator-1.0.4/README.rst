.. title

Evacuator
=========

|Repo Status| |PyPI License| |PyPI Python Version|
|Documentation| |Build Status| |Coverage| |pre-commit.ci|

.. |Repo Status| image:: https://www.repostatus.org/badges/latest/active.svg
    :target: https://github.com/MobileTeleSystems/evacuator
.. |PyPI License| image:: https://img.shields.io/pypi/l/evacuator.svg
    :target: https://github.com/MobileTeleSystems/evacuator/blob/develop/LICENSE.txt
.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/evacuator.svg
    :target: https://badge.fury.io/py/evacuator
.. |Build Status| image:: https://github.com/MobileTeleSystems/evacuator/workflows/Tests/badge.svg
    :target: https://github.com/MobileTeleSystems/evacuator/actions
.. |Documentation| image:: https://readthedocs.org/projects/evacuator/badge/?version=stable
    :target: https://evacuator.readthedocs.io/en/stable/
.. |Coverage| image:: https://codecov.io/gh/MobileTeleSystems/evacuator/branch/develop/graph/badge.svg?token=CM6AQWY65P
    :target: https://codecov.io/gh/MobileTeleSystems/evacuator
.. |pre-commit.ci| image:: https://results.pre-commit.ci/badge/github/MobileTeleSystems/evacuator/develop.svg
    :target: https://results.pre-commit.ci/latest/github/MobileTeleSystems/evacuator/develop

What is Evacuator?
------------------

Decorator/context manager designed to catch a certain exception and exit with specific exit code.

Designed to be used in `Apache Airflow <https://airflow.apache.org/>`__ with:
    * `BashOperator <https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/bash.html#skipping>`_ (`airflow>2.1`)
    * `PythonVirtualenvOperator <https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.PythonVirtualenvOperator>`_ (`airflow>=2.6`)
    * `ExternalPythonOperator <https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html#airflow.operators.python.ExternalPythonOperator>`_ (`airflow>=2.6`)
    * `DockerOperator <https://airflow.apache.org/docs/apache-airflow-providers-docker/stable/_api/airflow/providers/docker/operators/docker/index.html#airflow.providers.docker.operators.docker.DockerOperator>`_ (`apache-airflow-providers-docker>=3.5`)
    * `KubernetesPodOperator <https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/_api/airflow/providers/cncf/kubernetes/operators/pod/index.html#airflow.providers.cncf.kubernetes.operators.pod.KubernetesPodOperator>`_ (`apache-airflow-providers-cncf-kubernetes>=6.1`)
    * `SSHOperator <https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/_api/airflow/providers/ssh/operators/ssh/index.html#airflow.providers.ssh.operators.ssh.SSHOperator>`_ (`apache-airflow-providers-ssh>=3.10`)
    * any other operator support skipping task when process is exited with some specific exit code (``skip_on_exit_code`` option)

.. installation

How to install
---------------

.. code:: bash

    pip install evacuator

.. documentation

Documentation
-------------

See https://evacuator.readthedocs.io/

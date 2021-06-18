from nf_common_source.code.services.log_environment_utility_service.loggers.cpu_information_logger import log_all_cpu_information
from nf_common_source.code.services.log_environment_utility_service.loggers.cpu_information_logger import log_filtered_cpu_information
from nf_common_source.code.services.log_environment_utility_service.loggers.disk_information_logger import log_all_disk_information
from nf_common_source.code.services.log_environment_utility_service.loggers.environ_logger import log_all_environ_items
from nf_common_source.code.services.log_environment_utility_service.loggers.environ_logger import log_filtered_environ_items
from nf_common_source.code.services.log_environment_utility_service.loggers.memory_information_logger import log_all_memory_information
from nf_common_source.code.services.log_environment_utility_service.loggers.memory_information_logger import log_filtered_memory_information
from nf_common_source.code.services.log_environment_utility_service.loggers.network_information_logger import log_network_information
from nf_common_source.code.services.log_environment_utility_service.loggers.system_information_logger import log_all_system_items
from nf_common_source.code.services.log_environment_utility_service.loggers.system_information_logger import log_filtered_system_items
from nf_common_source.code.services.reporting_service.wrappers.run_and_log_function_wrapper import run_and_log_function


@run_and_log_function
def log_full_environment():

    log_all_environ_items()

    log_all_system_items()

    log_all_cpu_information()

    log_all_memory_information()

    log_all_disk_information()

    log_network_information()

@run_and_log_function
def log_filtered_environment():
    log_filtered_environ_items()

    log_filtered_system_items()

    log_filtered_cpu_information()

    log_filtered_memory_information()

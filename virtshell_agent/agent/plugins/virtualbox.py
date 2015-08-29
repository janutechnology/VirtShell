def run(logger, request):
    logger.info("Hello from a virtualbox plugin!!!!!!!!!!!!!!!")
    message = request.message
    logger.info(message)
    return 1
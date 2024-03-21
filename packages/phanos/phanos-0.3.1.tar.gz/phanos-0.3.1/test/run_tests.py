# run tests wit `python ./run_tests.py`

# coverage is in requirements-dev
# noinspection PyPackageRequirements
import coverage
import sys
import unittest
from os.path import join, dirname


ABSTRACT_CLASSES = [
    "phanos/publisher.py/SyncBaseHandler",
    "phanos.publisher.AsyncBaseHandler",
    "phanos.publisher.BasePublisher",
    "phanos.publisher.BaseHandler",
    "phanos.publisher.BaseFormatter",
]
src_path = join(join(dirname(__file__), ".."), "")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

if __name__ == "__main__":
    cov = coverage.Coverage(omit=["*/test/*", "*/log.py", *ABSTRACT_CLASSES])
    cov.start()
    # import after cov.start() due to correct coverage report
    from test import (
        test_tree,
        test_handlers,
        test_metrics,
        test_config,
        test_async,
        test_sync,
        test_messaging,
        test_publisher,
    )

    test_classes = [
        test_sync.TestProfiling,
        test_async.TestAsyncProfile,
        test_tree.TestContextTree,
        test_tree.TestContext,
        test_tree.TestMethodTreeNode,
        test_config.TestConfig,
        test_handlers.TestOutputFormatter,
        test_handlers.TestImpProfHandler,
        test_handlers.TestAsyncImpProfHandler,
        test_handlers.TestHandlers,
        test_metrics.TestStoreOperationDecorator,
        test_metrics.TestMetrics,
        test_messaging.TestBlockingPublisher,
        test_messaging.TestBasePublisher,
        test_messaging.TestAsyncPublisher,
        test_publisher.TestProfiler,
        test_publisher.TestSyncProfilerExt,
        test_publisher.TestAsyncProfilerExt,
    ]
    loader = unittest.TestLoader()
    class_suites = []
    for class_ in test_classes:
        suite = loader.loadTestsFromTestCase(class_)
        class_suites.append(suite)
    suite_ = unittest.TestSuite(class_suites)
    runner = unittest.TextTestRunner()
    results = runner.run(suite_)
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report()
    exit()

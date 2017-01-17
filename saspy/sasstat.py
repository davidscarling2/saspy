#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import logging
from saspy.sasproccommons import SASProcCommons


class SASstat:
    """
    This class is for SAS/STAT procedures to be called as python3 objects and use SAS as the computational engine
    This class and all the useful work in this package require a licensed version of SAS.
    To add a new procedure do the following:
    1. Create a new method for the procedure
    2. Create the set of required statements. If there are no required statements then create an empty set {}
    3. Create the legal set of statements. This can often be obtained from the documentation of the procedure.
        'procopts' should always be included in the legal set to allow flexibility in calling the procedure.
    4. Create the doc string with the following parts at a minimum:
        A. Procedure Name
        B. Required set
        C. Legal set
        D. Link to the procedure documentation
    5. Add the return call for the method using an existing procedure as an example
    6. Verify that all the statements in the required and legal sets are listed in _makeProcCallMacro method
        of sasproccommons.py
    7. Write at least one test to exercise the procedures and include it in the appropriate testing file
    """
    def __init__(self, session, *args, **kwargs):
        """
        Submit an initial set of macros to prepare the SAS system
        """
        self.sasproduct = "stat"
        # create logging
        # logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.WARN)
        self.sas = session
        logging.debug("Initialization of SAS Macro: " + self.sas.saslog())

    def hpsplit(self, **kwargs: dict) -> object:
        """
        Python method to call the HPSPLIT procedure

        required_set = {}
        legal_set= {'cls', 'code', 'grow', 'id', 'model', 'out'
                    'partition', 'performance', 'prune', 'rules'}
        For more information on the statements see the Documentation link.
        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/stathpug/68163/HTML/default/viewer.htm#stathpug_hpsplit_syntax.htm
        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {}
        legal_set = {'cls', 'code', 'grow', 'id', 'model', 'out',
                     'partition', 'performance', 'prune', 'rules', 'target', 'input', 'procopts'}
        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "HPSPLIT", required_set, legal_set, **kwargs)

    def reg(self, **kwargs: dict) -> object:
        """
        Python method to call the REG procedure
        For more information on the statements see the Documentation link.
        required_set={'model'}
        legal_set= {'add', 'by', 'code', 'id', 'var',
                    'lsmeans', 'model', 'random', 'repeated',
                    'slice', 'test', 'weight', 'out'}
        Documentation link:
        http://support.sas.com/documentation/cdl/en/statug/68162/HTML/default/viewer.htm#statug_reg_syntax.htm

        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {'model'}
        legal_set = {'add', 'by', 'code', 'id', 'var',
                     'lsmeans', 'model', 'random', 'repeated',
                     'slice', 'test', 'weight', 'out', 'procopts'}

        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "REG", required_set, legal_set, **kwargs)

    def mixed(self, **kwargs: dict) -> object:
        """
        Python method to call the MIXED procedure
        For more information on the statements see the Documentation link.
        required_set={'model'}
        legal_set= {'by', 'cls', 'code', 'contrast', 'estimate', 'id',
                    'lsmeans', 'model', 'out', 'random', 'repeated',
                    'slice', 'weight'}
        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/statug/68162/HTML/default/viewer.htm#statug_mixed_toc.htm

        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {'model'}
        legal_set = {'by', 'cls', 'code', 'contrast', 'estimate', 'id',
                     'lsmeans', 'model', 'out', 'random', 'repeated',
                     'slice', 'weight', 'procopts'}

        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "MIXED", required_set, legal_set, **kwargs)

    def glm(self, **kwargs: dict) -> object:
        """
        Python method to call the GLM procedure
        For more information on the statements see the Documentation link.
        required_set={'model'}
        legal_set= {'absorb', 'by', 'cls', 'contrast', 'estimate', 'freq', 'id',
                    'lsmeans', 'manova', 'means', 'model', 'out', 'random', 'repeated',
                    'test', 'weight'}

        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/statug/68162/HTML/default/viewer.htm#statug_glm_toc.htm

        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {'model'}
        legal_set = {'absorb', 'by', 'cls', 'contrast', 'estimate', 'freq', 'id',
                     'lsmeans', 'manova', 'means', 'model', 'out', 'random', 'repeated',
                     'test', 'weight', 'procopts'}

        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "GLM", required_set, legal_set, **kwargs)

    def logistic(self, **kwargs: dict) -> object:
        """
        Python method to call the LOGISTIC procedure
        For more information on the statements see the Documentation link.

        required_set={'model'}
        legal_set= {'by', 'cls', 'contrast', 'effect', 'effectplot', 'estimate',
                    'exact', 'freq', 'lsmeans', 'oddsratio', 'out', 'roc', 'score', 'slice',
                    'store', 'strata', 'units', 'weight'}

        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/statug/68162/HTML/default/viewer.htm#statug_logistic_toc.htm

        The PROC LOGISTIC and MODEL statements are required.
        The CLASS and EFFECT statements (if specified) must
        precede the MODEL statement, and the CONTRAST, EXACT,
        and ROC statements (if specified) must follow the MODEL
        statement.

        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {'model'}
        legal_set = {'by', 'cls', 'contrast', 'effect', 'effectplot', 'estimate',
                     'exact', 'freq', 'lsmeans', 'oddsratio', 'out', 'roc', 'score', 'slice',
                     'store', 'strata', 'units', 'weight', 'procopts'}

        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "LOGISTIC", required_set, legal_set, **kwargs)

    def tpspline(self, **kwargs: dict) -> object:
        """
        Python method to call the TPSPLINE procedure
        For more information on the statements see the Documentation link.

        required_set = {'model'}
        legal_set = {'by', 'freq', 'id', 'model', 'output', 'score', 'procopts'}

        cls is an alias for the class statement
        Documentation link:
        http://support.sas.com/documentation/cdl/en/statug/68162/HTML/default/viewer.htm#statug_tpspline_toc.htm

        The PROC TPSPLINE and MODEL statements are required.

        :param kwargs: dict
        :return: SAS result object
        """
        required_set = {'model'}
        legal_set = {'by', 'freq', 'id', 'model', 'output', 'score', 'procopts'}

        logging.debug("kwargs type: " + str(type(kwargs)))
        return SASProcCommons._run_proc(self, "TPSPLINE", required_set, legal_set, **kwargs)
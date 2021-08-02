node {
    try{
      def repoInformation = checkout scm
      def GIT_COMMIT_HASH = repoInformation.GIT_COMMIT


      def parallelTestConfiguration = [
        [
        '[test CREATE USER]': 'Api-testing-python-Qups-/testing/test_CREATE_USER',
        '[test DELAYED RESPONSE]': 'Api-testing-python-Qups-/testing/test_DELAYED_RESPONSE',
        '[test DELETE USER]': 'Api-testing-python-Qups-/testing/test_DELETE_USER',
        '[test GET USER]': 'Api-testing-python-Qups-/testing/test_GET_USER',
        '[test GET USERS LIST]': 'Api-testing-python-Qups-/testing/test_GET_USERS_LIST',
        '[test LIST Resource]': 'Api-testing-python-Qups-/testing/test_LIST_Resource',
        '[test Login Unsuccessful]': 'Api-testing-python-Qups-/testing/test_Login_Unsuccessful',
        '[test Patch]': 'Api-testing-python-Qups-/testing/test_Patch',
        '[test POST LOGIN SUCCESSFUL]': 'Api-testing-python-Qups-/testing/test_POST_LOGIN_SUCCESSFUL',
        '[test POST REGISTER SUCCESSFUL]': 'Api-testing-python-Qups-/testing/test_POST_REGISTER_SUCCESSFUL',
        '[test REGISTER UNSUCCESSFUL]': 'Api-testing-python-Qups-/testing/test_REGISTER_UNSUCCESSFUL',
        '[test SINGLE RESOURCE]': 'Api-testing-python-Qups-/testing/test_SINGLE_RESOURCE',
        '[test SINGLE RESOURCE NOT FOUND]': 'Api-testing-python-Qups-/testing/test_SINGLE_RESOURCE_NOT_FOUND',
        '[test SINGLE USER NOT FOUND]': 'Api-testing-python-Qups-/testing/test_SINGLE_USER_NOT_FOUND',
        '[test UPDATE USER]': 'Api-testing-python-Qups-/testing/test_UPDATE_USER',


        ]
      ]

      def stepList = prepareBuildStages(parallelTestConfiguration)

      for (def groupOfSteps in stepList) {
        parallel groupOfSteps
      }

    } catch(error) {
      echo "The following error occurred: ${error}"
      throw error
    } finally {
      allure([
        includeProperties: false,
        jdk: '',
        properties: [],
        reportBuildPolicy: 'ALWAYS',
        results: [[path: 'target/allure-results']]
      ])
    }
}


def prepareBuildStages(List<Map<String,String>> parallelTestConfiguration) {
  def stepList = []

  println('Preparing builds...')

  for (def parallelConfig in  parallelTestConfiguration) {
    def parallelSteps = prepareParallelSteps(parallelConfig)
    stepList.add(parallelSteps)
  }

  println(stepList)
  println('Finished preparing builds!')

  return stepList
}


def prepareParallelSteps(Map<String, String> parallelStepsConfig) {
  def parallelSteps = [:]
  for (def key in parallelStepsConfig.keySet()) {
    parallelSteps.put(key, prepareOneBuildStage(key, parallelStepsConfig[key]))
  }
  return parallelSteps
}

def prepareOneBuildStage(String name, String file) {
  return {
    stage("Test: ${name}") {
      println("Test: ${name}")
        withCredentials([
            string(credentialsId: 'pwd_jz_su', variable: 'pwd_jz_su'),
            string(credentialsId: 'db_pwd_aws', variable: 'db_pwd_aws'),
            string(credentialsId: 'selenium_grid_16ram', variable: 'selenium_grid_16ram'),
            ]) {
              // Tests go here
              sh """
                python3 -m pytest ${file}.py --alluredir=${WORKSPACE}/allure-results
              """
          }
    }
  }
}
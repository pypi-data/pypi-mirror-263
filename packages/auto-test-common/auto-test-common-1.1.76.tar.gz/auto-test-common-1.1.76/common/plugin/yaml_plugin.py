from os import path
from common.plugin.data_plugin import DataPlugin
from common.config.config import TEST_DATA_PATH
from common.file.handle_yaml import get_yaml_dict,get_yaml_data
from common.data.data_process import DataProcess
from common.common.constant import Constant
from common.plugin.data_bus import DataBus
from common.data.handle_common import print_debug

class YamlPlugin(object):

    @classmethod
    def load_data(self,file_name,file_path: str = TEST_DATA_PATH):
        DataBus.save_init_data()
        _path = path.join(file_path, file_name, )
        yamlData = get_yaml_data(_path)
        return yamlData

    @classmethod
    def get_dict(self,file_name, key:str=None, file_path: str = TEST_DATA_PATH):
        DataBus.save_init_data()
        file_name = path.join(file_path, file_name, )
        yamlData = get_yaml_dict(file_name, key)
        return yamlData

    @classmethod
    def get_data(self,file_name,  dict: dict = None, _replace: bool=True, file_path: str = TEST_DATA_PATH,_remove_null:bool=False,_no_content =0) -> "list":
        DataBus.save_init_data()
        file_name = path.join(file_path, file_name, )
        yamlData = self.get_dict(file_name)
        datas = DataProcess.check_test_data(yamlData)
        datas = DataProcess.list_dict_duplicate_removal_byKey(datas, Constant.CASE_TITLE)
        datas = DataProcess.list_dict_duplicate_removal_byKey(datas, Constant.CASE_NO)
        _datas = []
        for _temp in datas:
            _data = {}
            for key in _temp.keys():
                _data[key] = DataPlugin.checkData(_temp[key], dict, _replace, _remove_null, _no_content)
                if key == Constant.TEST_DATA:
                    for _key in _data[Constant.TEST_DATA].keys():
                        _data[_key] = DataPlugin.checkData(_data[Constant.TEST_DATA][_key], dict, _replace, _remove_null, _no_content)
            _datas.append(_data)
        print_debug("最终参数化测试数据:"+str(_datas))
        return _datas



if __name__ == '__main__':
    _scriptPath= [{'id': 525266, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】修改中文姓名成功', 'caserunid': '1422380', 'caseid': 'CB24083-927', 'status': '失败', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_03', 'service': ''}, {'id': 525267, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】会员国籍为CN，修改英文姓名成功', 'caserunid': '1422381', 'caseid': 'CB24083-928', 'status': '失败', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_04', 'service': ''}, {'id': 525268, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】修改中文姓名-中文姓有值中文名为空，修改失败', 'caserunid': '1422382', 'caseid': 'CB24083-929', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_single/test_enrollMember.py', 'script': 'test/test_single/test_enrollMember.py::TestEnrollMember::test_memberInformationModification[params2]', 'service': ''}, {'id': 525273, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】会员国籍为ZZ，修改英文姓名成功，会员国籍更新为CN', 'caserunid': '1422387', 'caseid': 'CB24083-934', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_05', 'service': ''}, {'id': 525275, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】会员国籍为XX，修改英文姓名成功，会员国籍更新为CN', 'caserunid': '1422389', 'caseid': 'CB24083-936', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_06', 'service': ''}, {'id': 525276, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】会员国籍为空，修改英文姓名成功，会员国籍更新为CN', 'caserunid': '1422390', 'caseid': 'CB24083-937', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_07', 'service': ''}, {'id': 525285, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】会员存在无效手机号，根据凭证修改会员手机号成功后，可修改英文姓名成功', 'caserunid': '1422399', 'caseid': 'CB24083-951', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_09', 'service': ''}, {'id': 525290, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-根据凭证修改会员信息】会员账户内无中文姓名、证件类型无身份证、国籍非CN/ZZ/XX/空，修改中文姓名成功', 'caserunid': '1422404', 'caseid': 'CB24083-972', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_scene/test_api_updateMemberVerify02.py', 'script': 'test/test_scene/test_api_updateMemberVerify02.py::TestApiUpdateMemberVerify02::test_08', 'service': ''}, {'id': 525291, 'jirakey': 'CB24083-833', 'cycleId': '29885', 'cyclename': '1', 'casename': '【MUFL接口-查询会员详细信息和偏好资料】响应参数增加【修改英文姓名次数】字段，并反馈该会员已修改英文姓名的次数', 'caserunid': '1422405', 'caseid': 'CB24083-948', 'status': '通过', 'create_time': '2024-03-19 10:44:44', 'desc': 'http://172.28.22.90/autotest/consumer-services/frequent-flyer-api/-/blob/master/test/test_single/test_enrollMember.py', 'script': 'test/test_single/test_enrollMember.py::TestEnrollMember::test_queryMemberInformation[params17]', 'service': ''}]
    _listscript = list(map(lambda x: x['script'].split('[')[0], _scriptPath))
    _listscript.sort()
    print(str(_listscript))



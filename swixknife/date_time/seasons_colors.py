
import collections

from ..sezimal import SezimalInteger
from ..functions import SezimalRange
from .sun_moon import list_sun_moon
from .sezimal_functions import ZoneInfo


_WEEKLY_SEASON_COLOR_CACHE = {}
_WEEKLY_SEASON_GRAY_CACHE = {}

#
# Season’s color gradations, for 20 weeks, 21 and 22
# season’s length;
# Colors are material color shades,
# amber for summer,
# pink or autumn,
# light blu for winter,
# and light green for spring
#

_SHADES = ('50', '100', '200', '300', '400', '500', '600', '700', '800', '900') #, 'A100', 'A200', 'A400', 'A700')


class SezimalDictionary(collections.OrderedDict):
    def __getitem__(self, key):
        if type(key) == int:
            key = SezimalInteger(key)

        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if type(key) == int:
            key = SezimalInteger(key)

        return super().__setitem__(key, value)

    # def __getattr__(self, key):
    #     if type(key) == int:
    #         key = SezimalInteger(key)
    #
    #     return super().__getattr__(key)
    #
    # def __setattr__(self, key, value):
    #     if type(key) == int:
    #         key = SezimalInteger(key)
    #
    #     return super().__setattr__(key, value)


_WEEKS_SHADE_SEASON_COLOR_GRADATION = SezimalDictionary({
    SezimalInteger('14'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff6e2', '#fef4e3', '#fef3e4', '#fef1e5', '#feefe6', '#fdede7', '#fdebe8', '#fde9e9', '#fde8ea', '#fce6eb',
            ],
            'autumn': [
                '#fce4ec', '#fae6ee', '#f7e7ef', '#f5e9f1', '#f2eaf3', '#f0ecf4', '#ededf6', '#ebeff7', '#e8f0f9', '#e6f2fb', '#e3f3fc',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e2f5fa', '#e3f5f8', '#e4f5f6', '#e4f5f4', '#e5f5f3', '#e5f5f1', '#e6f5ef', '#e7f5ed', '#e7f5eb',
            ],
            'spring': [
                '#e8f5e9', '#eaf5e8', '#ecf6e8', '#eef6e7', '#f0f6e6', '#f2f6e5', '#f5f7e5', '#f7f7e4', '#f9f7e3', '#fbf7e2', '#fdf8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee8b6', '#fee3b8', '#fddfbb', '#fcdabe', '#fcd6c0', '#fbd1c3', '#fbcdc5', '#fac8c8', '#f9c4cb', '#f9bfcd',
            ],
            'autumn': [
                '#f8bbd0', '#f2bfd4', '#ebc3d8', '#e5c6dc', '#dfcae0', '#d9cee4', '#d2d2e8', '#ccd6ec', '#c6daf0', '#c0ddf4', '#b9e1f8',
            ],
            'winter': [
                '#b3e5fc', '#b5e5f7', '#b7e5f3', '#b9e5ee', '#bbe5e9', '#bde5e5', '#bee6e0', '#c0e6dc', '#c2e6d7', '#c4e6d2', '#c6e6ce',
            ],
            'spring': [
                '#c8e6c9', '#cde7c7', '#d2e7c5', '#d7e8c3', '#dce8c1', '#e1e9bf', '#e6e9bd', '#ebeabb', '#f0eab9', '#f5ebb7', '#faebb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fed986', '#fdd18b', '#fcca8f', '#fbc393', '#fabb97', '#f9b49c', '#f8aca0', '#f7a5a4', '#f69ea8', '#f596ad',
            ],
            'autumn': [
                '#f48fb1', '#ea95b8', '#df9cbe', '#d5a2c5', '#caa8cc', '#c0aed2', '#b5b5d9', '#abbbdf', '#a0c1e6', '#96c7ed', '#8bcef3',
            ],
            'winter': [
                '#81d4fa', '#84d4f2', '#88d4eb', '#8bd5e3', '#8ed5dc', '#91d5d4', '#95d5cd', '#98d5c5', '#9bd5be', '#9ed6b6', '#a2d6af',
            ],
            'spring': [
                '#a5d6a7', '#add7a4', '#b5d8a0', '#bed99d', '#c6da9a', '#cedb96', '#d6db93', '#dedc8f', '#e6dd8c', '#efde89', '#f7df85',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecb55', '#fcc05b', '#fbb661', '#faab67', '#f8a16d', '#f79674', '#f58c7a', '#f48180', '#f37786', '#f16c8c',
            ],
            'autumn': [
                '#f06292', '#e16b9b', '#d374a4', '#c47cae', '#b585b7', '#a78ec0', '#9897c9', '#8aa0d2', '#7ba9db', '#6cb1e5', '#5ebaee',
            ],
            'winter': [
                '#4fc3f7', '#54c3ed', '#58c4e2', '#5dc4d8', '#61c4cd', '#66c5c3', '#6ac5b8', '#6fc6ae', '#73c6a3', '#78c699', '#7cc78e',
            ],
            'spring': [
                '#81c784', '#8cc87f', '#98ca7a', '#a3cb76', '#afcc71', '#bacd6c', '#c6cf67', '#d1d062', '#ddd15d', '#e8d259', '#f4d454',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fdbd2f', '#fcb137', '#faa43e', '#f89846', '#f68b4d', '#f57f55', '#f3725c', '#f16664', '#ef596b', '#ee4d73',
            ],
            'autumn': [
                '#ec407a', '#da4b85', '#c95591', '#b7609c', '#a56ba7', '#9376b2', '#8280be', '#708bc9', '#5e96d4', '#4ca1df', '#3babeb',
            ],
            'winter': [
                '#29b6f6', '#2fb6e9', '#34b7dd', '#3ab7d0', '#3fb8c3', '#45b8b6', '#4ab9aa', '#50b99d', '#55ba90', '#5bba83', '#60bb77',
            ],
            'spring': [
                '#66bb6a', '#74bc64', '#82be5e', '#90bf58', '#9ec052', '#acc24c', '#b9c346', '#c7c540', '#d5c63a', '#e3c734', '#f1c92e',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb20f', '#fba318', '#f99520', '#f78628', '#f57731', '#f36839', '#f15942', '#ef4a4a', '#ed3c52', '#eb2d5b',
            ],
            'autumn': [
                '#e91e63', '#d42b70', '#bf377d', '#aa448b', '#955198', '#805da5', '#6c6ab2', '#5776bf', '#4283cc', '#2d90da', '#189ce7',
            ],
            'winter': [
                '#03a9f4', '#0aaae5', '#10aad6', '#17abc7', '#1eabb8', '#24aca9', '#2bac9b', '#31ad8c', '#38ad7d', '#3fae6e', '#45ae5f',
            ],
            'spring': [
                '#4caf50', '#5cb149', '#6db243', '#7db43c', '#8db635', '#9db72f', '#aeb928', '#beba22', '#cebc1b', '#debe14', '#efbf0e',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fba509', '#f89711', '#f48a1a', '#f17c23', '#ed6e2c', '#ea6034', '#e6523d', '#e34446', '#df374f', '#dc2957',
            ],
            'autumn': [
                '#d81b60', '#c5276c', '#b13278', '#9e3e84', '#8b4a90', '#77559c', '#6461a9', '#506cb5', '#3d78c1', '#2a84cd', '#168fd9',
            ],
            'winter': [
                '#039be5', '#099bd7', '#0f9cc8', '#149cba', '#1a9dac', '#209d9d', '#269e8f', '#2c9e80', '#329f72', '#379f64', '#3da055',
            ],
            'spring': [
                '#43a047', '#54a241', '#65a33a', '#76a534', '#87a72d', '#98a927', '#aaaa20', '#bbac1a', '#ccae13', '#ddb00d', '#eeb106',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#f99408', '#f48711', '#ee7b19', '#e96f21', '#e36229', '#de5632', '#d8493a', '#d33d42', '#cd314a', '#c82453',
            ],
            'autumn': [
                '#c2185b', '#b12266', '#9f2c70', '#8e377b', '#7c4186', '#6b4b91', '#59559b', '#485fa6', '#3669b1', '#2574bc', '#137ec6',
            ],
            'winter': [
                '#0288d1', '#0789c3', '#0c89b6', '#118aa8', '#168a9b', '#1b8b8d', '#1f8b80', '#248c72', '#298c65', '#2e8d57', '#338d4a',
            ],
            'spring': [
                '#388e3c', '#4a9037', '#5c9131', '#6e932c', '#809526', '#929621', '#a5981b', '#b79916', '#c99b10', '#db9d0b', '#ed9e05',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f88408', '#f07910', '#e96d18', '#e16220', '#da5728', '#d24c2f', '#cb4137', '#c3363f', '#bc2a47', '#b41f4f',
            ],
            'autumn': [
                '#ad1457', '#9d1d60', '#8e266a', '#7e2f73', '#6f387c', '#5f4185', '#504a8f', '#405398', '#315ca1', '#2165aa', '#126eb4',
            ],
            'winter': [
                '#0277bd', '#0678b0', '#0a78a4', '#0e7997', '#12798a', '#167a7e', '#1a7a71', '#1e7b65', '#227b58', '#267c4b', '#2a7c3f',
            ],
            'spring': [
                '#2e7d32', '#417f2d', '#548029', '#678224', '#7a8420', '#8d851b', '#a08717', '#b38812', '#c68a0e', '#d98c09', '#ec8d05',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f46607', '#e95d0e', '#df5516', '#d44c1d', '#c94324', '#be3a2b', '#b33132', '#a82839', '#9e2041', '#931748',
            ],
            'autumn': [
                '#880e4f', '#7c1556', '#6f1b5d', '#632264', '#57296b', '#4b2f72', '#3e3678', '#323c7f', '#264386', '#1a4a8d', '#0d5094',
            ],
            'winter': [
                '#01579b', '#035890', '#065885', '#085979', '#0a5a6e', '#0d5a63', '#0f5b58', '#125b4d', '#145c42', '#165d36', '#195d2b',
            ],
            'spring': [
                '#1b5e20', '#30601d', '#44611a', '#596317', '#6e6414', '#836611', '#97670f', '#ac690c', '#c16a09', '#d66c06', '#ea6d03',
            ],
        },
    },
    SezimalInteger('15'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff6e2', '#fef5e3', '#fef3e4', '#fef1e5', '#fef0e6', '#feeee6', '#fdece7', '#fdebe8', '#fde9e9', '#fce7ea', '#fce6eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ee', '#f8e7ef', '#f5e8f0', '#f3eaf2', '#f1ebf3', '#eeecf5', '#eceef6', '#eaeff8', '#e8f1fa', '#e6f2fb', '#e3f4fc',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e2f5fb', '#e3f5f9', '#e3f5f7', '#e4f5f5', '#e4f5f3', '#e5f5f2', '#e6f5f0', '#e6f5ee', '#e7f5ec', '#e7f5eb',
            ],
            'spring': [
                '#e8f5e9', '#eaf5e8', '#ecf6e8', '#eef6e7', '#f0f6e6', '#f2f6e6', '#f3f6e5', '#f5f7e4', '#f7f7e4', '#f9f7e3', '#fbf8e2', '#fdf8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee8b5', '#fee4b8', '#fde0ba', '#fddcbd', '#fcd8bf', '#fcd3c2', '#fbcfc4', '#facbc6', '#fac7c9', '#f9c3cb', '#f9bfce',
            ],
            'autumn': [
                '#f8bbd0', '#f2bed4', '#ecc2d7', '#e7c5db', '#e1c9df', '#dbcce2', '#d5d0e6', '#d0d3ea', '#cad7ed', '#c4dbf1', '#bedef5', '#b9e2f8',
            ],
            'winter': [
                '#b3e5fc', '#b5e5f8', '#b6e5f4', '#b8e5ef', '#bae5eb', '#bce5e7', '#bee6e2', '#bfe6de', '#c1e6da', '#c3e6d6', '#c4e6d2', '#c6e6cd',
            ],
            'spring': [
                '#c8e6c9', '#cde6c7', '#d1e7c5', '#d6e8c3', '#dae8c2', '#dfe8c0', '#e3e9be', '#e8eabc', '#edeaba', '#f1eab8', '#f6ebb7', '#faecb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fed986', '#fdd38a', '#fccc8e', '#fbc592', '#fabe96', '#fab89a', '#f9b19d', '#f8aaa1', '#f7a3a5', '#f69ca9', '#f596ad',
            ],
            'autumn': [
                '#f48fb1', '#ea95b7', '#e19bbd', '#d7a0c3', '#cea6c9', '#c4accf', '#bbb2d5', '#b1b7dc', '#a7bde2', '#9ec3e8', '#94c9ee', '#8bcef4',
            ],
            'winter': [
                '#81d4fa', '#84d4f3', '#87d4ec', '#8ad4e5', '#8dd5de', '#90d5d7', '#93d5d0', '#96d5ca', '#99d5c3', '#9cd6bc', '#9fd6b5', '#a2d6ae',
            ],
            'spring': [
                '#a5d6a7', '#acd7a4', '#b4d8a1', '#bcd89e', '#c3d99b', '#cbda98', '#d2db94', '#dadc91', '#e1dd8e', '#e8de8b', '#f0de88', '#f8df85',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecb55', '#fcc25a', '#fbb860', '#faaf65', '#f9a56b', '#f89c70', '#f69276', '#f5887c', '#f47f81', '#f27587', '#f16c8c',
            ],
            'autumn': [
                '#f06292', '#e36a9a', '#d572a3', '#c87aab', '#ba82b4', '#ad8abc', '#a092c4', '#929bcd', '#85a3d5', '#77abde', '#6ab3e6', '#5cbbef',
            ],
            'winter': [
                '#4fc3f7', '#53c3ed', '#57c4e4', '#5cc4da', '#60c4d1', '#64c5c7', '#68c5be', '#6cc5b4', '#70c6aa', '#74c6a1', '#79c697', '#7dc78e',
            ],
            'spring': [
                '#81c784', '#8bc880', '#96c97b', '#a0cb77', '#abcc72', '#b5cd6e', '#c0ce6a', '#cbcf65', '#d5d061', '#e0d25c', '#ead358', '#f4d453',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fdbe2f', '#fcb336', '#faa83c', '#f99c43', '#f7904a', '#f68551', '#f47a58', '#f26e5f', '#f16266', '#ef576c', '#ee4c73',
            ],
            'autumn': [
                '#ec407a', '#dc4a84', '#cc548f', '#bb5e99', '#ab67a3', '#9b71ae', '#8b7bb8', '#7a85c2', '#6a8fcd', '#5a98d7', '#4aa2e1', '#39acec',
            ],
            'winter': [
                '#29b6f6', '#2eb6ea', '#33b7df', '#38b7d3', '#3db8c7', '#42b8bc', '#48b8b0', '#4db9a4', '#52b999', '#57ba8d', '#5cba81', '#61bb76',
            ],
            'spring': [
                '#66bb6a', '#73bc64', '#80bd5f', '#8cbf5a', '#99c054', '#a6c14e', '#b2c249', '#bfc444', '#ccc53e', '#d9c638', '#e6c833', '#f2c92e',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb30f', '#fba616', '#fa981e', '#f88b26', '#f67d2d', '#f47035', '#f2623d', '#f05444', '#ee474c', '#ed3954', '#eb2c5b',
            ],
            'autumn': [
                '#e91e63', '#d62a6f', '#c3357b', '#b04187', '#9c4c93', '#89589f', '#7664ac', '#636fb8', '#507bc4', '#3c86d0', '#2992dc', '#169de8',
            ],
            'winter': [
                '#03a9f4', '#09aae6', '#0faad9', '#15abcb', '#1babbd', '#21acb0', '#28aca2', '#2eac94', '#34ad87', '#3aad79', '#40ae6b', '#46ae5e',
            ],
            'spring': [
                '#4caf50', '#5bb04a', '#6ab244', '#79b33e', '#88b538', '#97b632', '#a6b82c', '#b4ba25', '#c3bb1f', '#d2bc19', '#e1be13', '#f0c00d',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca608', '#f99a10', '#f58d18', '#f28020', '#ef7428', '#ec6730', '#e85a38', '#e54e40', '#e24148', '#de3450', '#db2858',
            ],
            'autumn': [
                '#d81b60', '#c6266b', '#b43076', '#a33b81', '#91468c', '#7f5097', '#6e5ba2', '#5c66ae', '#4a70b9', '#387bc4', '#2686cf', '#1590da',
            ],
            'winter': [
                '#039be5', '#089bd8', '#0e9ccb', '#139cbe', '#189db0', '#1e9da3', '#239e96', '#289e89', '#2e9e7c', '#339f6e', '#389f61', '#3ea054',
            ],
            'spring': [
                '#43a047', '#53a241', '#62a33b', '#72a535', '#82a62f', '#91a829', '#a1aa24', '#b1ab1e', '#c0ad18', '#d0ae12', '#e0b00c', '#efb106',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fa9508', '#f5890f', '#f07e17', '#eb731e', '#e66726', '#e05c2e', '#db5135', '#d6453d', '#d13a44', '#cc2f4c', '#c72353',
            ],
            'autumn': [
                '#c2185b', '#b22165', '#a22b6f', '#923478', '#823d82', '#72478c', '#625096', '#5259a0', '#4263aa', '#326cb4', '#2275bd', '#127fc7',
            ],
            'winter': [
                '#0288d1', '#0688c5', '#0b89b8', '#108aac', '#148a9f', '#188a93', '#1d8b86', '#228c7a', '#268c6e', '#2a8c61', '#2f8d55', '#338e48',
            ],
            'spring': [
                '#388e3c', '#499037', '#599132', '#6a922d', '#7a9428', '#8b9523', '#9c971e', '#ac9819', '#bd9a14', '#cd9c0f', '#de9d0a', '#ee9e05',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f88507', '#f17a0e', '#eb7016', '#e4661d', '#dd5c24', '#d6522c', '#cf4733', '#c83d3a', '#c23341', '#bb2849', '#b41e50',
            ],
            'autumn': [
                '#ad1457', '#9f1c60', '#912468', '#822d70', '#743579', '#663d82', '#58468a', '#494e92', '#3b569b', '#2d5ea4', '#1e66ac', '#106fb4',
            ],
            'winter': [
                '#0277bd', '#0678b1', '#0978a6', '#0d789a', '#11798f', '#147a83', '#187a78', '#1c7a6c', '#1f7b60', '#237b55', '#277c49', '#2a7c3e',
            ],
            'spring': [
                '#2e7d32', '#3f7e2e', '#51802a', '#628226', '#748321', '#85841d', '#968619', '#a88815', '#b98911', '#cb8a0c', '#dc8c08', '#ee8d04',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f56707', '#eb5f0d', '#e15714', '#d74f1a', '#cd4721', '#c33f28', '#ba362e', '#b02e35', '#a6263b', '#9c1e42', '#921648',
            ],
            'autumn': [
                '#880e4f', '#7d1455', '#721a5c', '#662062', '#5b2668', '#502c6f', '#443375', '#39397b', '#2e3f82', '#234588', '#174b8e', '#0c5195',
            ],
            'winter': [
                '#01579b', '#035891', '#055886', '#08597c', '#0a5972', '#0c5a68', '#0e5a5e', '#105b53', '#125c49', '#145c3f', '#175d34', '#195d2a',
            ],
            'spring': [
                '#1b5e20', '#2e5f1d', '#41611b', '#546218', '#676415', '#7a6513', '#8d6610', '#a0680d', '#b3690b', '#c66b08', '#d96c05', '#ec6e03',
            ],
        },
    },
    SezimalInteger('20'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff6e2', '#fff5e3', '#fef3e4', '#fef2e4', '#fef0e5', '#feefe6', '#fdede7', '#fdece8', '#fdeae9', '#fde9e9', '#fce7ea', '#fce6eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f8e7ef', '#f6e8f0', '#f4e9f2', '#f2ebf3', '#f0ecf4', '#ededf6', '#ebeef7', '#e9f0f8', '#e7f1fa', '#e5f2fb', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e2f5fb', '#e3f5f9', '#e3f5f8', '#e4f5f6', '#e4f5f4', '#e5f5f3', '#e5f5f1', '#e6f5ef', '#e6f5ee', '#e7f5ec', '#e7f5eb',
            ],
            'spring': [
                '#e8f5e9', '#eaf5e8', '#ecf5e8', '#edf6e7', '#eff6e7', '#f1f6e6', '#f3f6e5', '#f4f7e5', '#f6f7e4', '#f8f7e3', '#faf7e3', '#fbf8e2', '#fdf8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee8b5', '#fee4b7', '#fde1ba', '#fdddbc', '#fcd9be', '#fcd5c0', '#fbd2c3', '#fbcec5', '#facac7', '#fac6c9', '#f9c3cc', '#f9bfce',
            ],
            'autumn': [
                '#f8bbd0', '#f3bed3', '#edc1d7', '#e8c5da', '#e3c8de', '#ddcbe1', '#d8cee4', '#d3d2e8', '#ced5eb', '#c8d8ee', '#c3dbf2', '#bedff5', '#b8e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b5e5f8', '#b6e5f4', '#b8e5f0', '#b9e5ec', '#bbe5e8', '#bde5e4', '#bee6e1', '#c0e6dd', '#c2e6d9', '#c3e6d5', '#c5e6d1', '#c6e6cd',
            ],
            'spring': [
                '#c8e6c9', '#cce6c7', '#d0e7c6', '#d5e7c4', '#d9e8c2', '#dde8c1', '#e1e9bf', '#e6e9bd', '#eaeabb', '#eeeaba', '#f2ebb8', '#f7ebb6', '#fbecb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#feda86', '#fdd489', '#fccd8d', '#fcc790', '#fbc194', '#fabb98', '#f9b49b', '#f8ae9f', '#f7a8a3', '#f7a2a6', '#f69baa', '#f595ad',
            ],
            'autumn': [
                '#f48fb1', '#eb94b7', '#e29abc', '#d99fc2', '#d1a4c7', '#c8aacd', '#bfafd3', '#b6b4d8', '#adb9de', '#a4bfe4', '#9cc4e9', '#93c9ef', '#8acff4',
            ],
            'winter': [
                '#81d4fa', '#84d4f4', '#87d4ed', '#89d4e7', '#8cd5e0', '#8fd5da', '#92d5d4', '#94d5cd', '#97d5c7', '#9ad5c1', '#9dd6ba', '#9fd6b4', '#a2d6ad',
            ],
            'spring': [
                '#a5d6a7', '#acd7a4', '#b3d8a1', '#bad89e', '#c1d99c', '#c8da99', '#cfdb96', '#d5db93', '#dcdc90', '#e3dd8d', '#eade8b', '#f1de88', '#f8df85',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecc54', '#fdc359', '#fcba5e', '#fab264', '#f9a969', '#f8a06e', '#f79773', '#f68e78', '#f5857d', '#f37d83', '#f27488', '#f16b8d',
            ],
            'autumn': [
                '#f06292', '#e4699a', '#d771a2', '#cb78a9', '#be80b1', '#b287b9', '#a68fc1', '#9996c8', '#8d9ed0', '#81a5d8', '#74ade0', '#68b4e7', '#5bbcef',
            ],
            'winter': [
                '#4fc3f7', '#53c3ee', '#57c4e5', '#5bc4dc', '#5ec4d4', '#62c5cb', '#66c5c2', '#6ac5b9', '#6ec5b0', '#72c6a7', '#75c69f', '#79c696', '#7dc78d',
            ],
            'spring': [
                '#81c784', '#8bc880', '#94c97c', '#9eca78', '#a8cb74', '#b1cc70', '#bbcd6c', '#c5cf67', '#cfd063', '#d8d15f', '#e2d25b', '#ecd357', '#f5d453',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#febf2e', '#fcb535', '#fbaa3b', '#f9a041', '#f89548', '#f68a4e', '#f58054', '#f3755a', '#f26a61', '#f06067', '#ef556d', '#ed4b74',
            ],
            'autumn': [
                '#ec407a', '#dd4984', '#ce528d', '#bf5b97', '#b064a0', '#a16daa', '#9276b3', '#8380bd', '#7489c6', '#6592d0', '#569bd9', '#47a4e3', '#38adec',
            ],
            'winter': [
                '#29b6f6', '#2eb6eb', '#32b7e0', '#37b7d6', '#3cb8cb', '#40b8c0', '#45b8b5', '#4ab9ab', '#4fb9a0', '#53b995', '#58ba8a', '#5dba80', '#61bb75',
            ],
            'spring': [
                '#66bb6a', '#72bc65', '#7ebd60', '#89be5b', '#95c056', '#a1c151', '#adc24c', '#b8c346', '#c4c441', '#d0c53c', '#dcc737', '#e7c832', '#f3c92d',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb40e', '#fca815', '#fa9b1c', '#f88f23', '#f7822a', '#f57631', '#f36939', '#f15d40', '#f05047', '#ee444e', '#ec3755', '#eb2b5c',
            ],
            'autumn': [
                '#e91e63', '#d7296e', '#c63379', '#b43e84', '#a24990', '#91539b', '#7f5ea6', '#6d69b1', '#5b74bc', '#4a7ec7', '#3889d3', '#2694de', '#159ee9',
            ],
            'winter': [
                '#03a9f4', '#09a9e7', '#0eaadb', '#14aace', '#19abc2', '#1fabb5', '#25aca8', '#2aac9c', '#30ad8f', '#36ad82', '#3bae76', '#41ae69', '#46af5d',
            ],
            'spring': [
                '#4caf50', '#5ab04a', '#68b245', '#75b33f', '#83b53a', '#91b634', '#9fb72e', '#acb929', '#baba23', '#c8bb1d', '#d6bd18', '#e3be12', '#f1c00d',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca707', '#f99c0f', '#f69016', '#f3841e', '#f07925', '#ed6d2c', '#ea6134', '#e7553b', '#e44a42', '#e13e4a', '#de3251', '#db2759',
            ],
            'autumn': [
                '#d81b60', '#c8256a', '#b72f74', '#a7397f', '#964289', '#864c93', '#76569d', '#6560a8', '#556ab2', '#4574bc', '#347dc6', '#2487d1', '#1391db',
            ],
            'winter': [
                '#039be5', '#089bd9', '#0d9ccd', '#129cc1', '#179db4', '#1c9da8', '#219d9c', '#259e90', '#2a9e84', '#2f9e78', '#349f6b', '#399f5f', '#3ea053',
            ],
            'spring': [
                '#43a047', '#51a142', '#60a33c', '#6ea437', '#7da631', '#8ba72c', '#9aa926', '#a8aa21', '#b7ac1b', '#c5ad16', '#d4af10', '#e2b00b', '#f1b205',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fa9607', '#f68b0e', '#f18115', '#ec761c', '#e86c23', '#e3612a', '#de5731', '#d94c38', '#d5423f', '#d03746', '#cb2d4d', '#c72254',
            ],
            'autumn': [
                '#c2185b', '#b32164', '#a4296d', '#963276', '#873a7f', '#784388', '#694c91', '#5b549b', '#4c5da4', '#3d66ad', '#2e6eb6', '#2077bf', '#117fc8',
            ],
            'winter': [
                '#0288d1', '#0688c6', '#0a89ba', '#0e89af', '#138aa3', '#178a98', '#1b8b8c', '#1f8b81', '#238c75', '#278c6a', '#2c8d5e', '#308d53', '#348e47',
            ],
            'spring': [
                '#388e3c', '#478f37', '#579133', '#66922e', '#75942a', '#859525', '#949620', '#a3981c', '#b29917', '#c29a12', '#d19c0e', '#e09d09', '#f09f05',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f98607', '#f27c0d', '#ec7314', '#e6691b', '#df6021', '#d95628', '#d34d2f', '#cd4336', '#c63a3c', '#c03043', '#ba274a', '#b31d50',
            ],
            'autumn': [
                '#ad1457', '#a01c5f', '#932367', '#862b6f', '#783276', '#6b3a7e', '#5e4286', '#51498e', '#445196', '#37599e', '#2960a5', '#1c68ad', '#0f6fb5',
            ],
            'winter': [
                '#0277bd', '#0577b2', '#0978a8', '#0c789d', '#107992', '#137988', '#167a7d', '#1a7a72', '#1d7b67', '#207b5d', '#247c52', '#277c47', '#2b7d3d',
            ],
            'spring': [
                '#2e7d32', '#3e7e2e', '#4e802a', '#5e8126', '#6e8323', '#7e841f', '#8e851b', '#9f8717', '#af8813', '#bf890f', '#cf8b0c', '#df8c08', '#ef8e04',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f66806', '#ed600c', '#e45912', '#da5118', '#d14a1e', '#c84224', '#bf3b2b', '#b63331', '#ad2c37', '#a3243d', '#9a1d43', '#911549',
            ],
            'autumn': [
                '#880e4f', '#7e1455', '#73195b', '#691f61', '#5e2466', '#542a6c', '#4a3072', '#3f3578', '#353b7e', '#2b4184', '#204689', '#164c8f', '#0b5195',
            ],
            'winter': [
                '#01579b', '#035892', '#055888', '#07597f', '#095975', '#0b5a6c', '#0d5a62', '#0f5b59', '#115b4f', '#135c46', '#155c3c', '#175d33', '#195d29',
            ],
            'spring': [
                '#1b5e20', '#2d5f1e', '#3e611b', '#506219', '#616316', '#736514', '#846611', '#96670f', '#a7680c', '#b96a0a', '#ca6b07', '#dc6c05', '#ed6e02',
            ],
        },
    },
    SezimalInteger('21'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff7e2', '#fff5e3', '#fef4e3', '#fef2e4', '#fef1e5', '#feefe6', '#feeee6', '#fdede7', '#fdebe8', '#fdeae9', '#fde8ea', '#fce7ea', '#fce5eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f8e6ef', '#f6e8f0', '#f4e9f1', '#f2eaf2', '#f0ebf4', '#eeecf5', '#edeef6', '#ebeff8', '#e9f0f9', '#e7f1fa', '#e5f3fb', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e2f5fb', '#e2f5fa', '#e3f5f8', '#e3f5f6', '#e4f5f5', '#e4f5f3', '#e5f5f2', '#e5f5f0', '#e6f5ef', '#e6f5ee', '#e7f5ec', '#e8f5ea',
            ],
            'spring': [
                '#e8f5e9', '#eaf5e8', '#ebf5e8', '#edf6e7', '#eff6e7', '#f0f6e6', '#f2f6e6', '#f3f6e5', '#f5f7e4', '#f7f7e4', '#f8f7e3', '#faf7e3', '#fcf8e2', '#fdf8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee9b5', '#fee5b7', '#fee2b9', '#fddebb', '#fcdbbd', '#fcd7bf', '#fcd3c2', '#fbd0c4', '#faccc6', '#fac9c8', '#fac5ca', '#f9c2cc', '#f8bece',
            ],
            'autumn': [
                '#f8bbd0', '#f3bed3', '#eec1d6', '#e9c4d9', '#e4c7dd', '#dfcae0', '#dacde3', '#d5d0e6', '#d1d3e9', '#ccd6ec', '#c7d9ef', '#c2dcf3', '#bddff6', '#b8e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b4e5f8', '#b6e5f5', '#b7e5f1', '#b9e5ed', '#bae5ea', '#bce5e6', '#bee6e2', '#bfe6df', '#c0e6db', '#c2e6d8', '#c4e6d4', '#c5e6d0', '#c6e6cd',
            ],
            'spring': [
                '#c8e6c9', '#cce6c7', '#d0e7c6', '#d4e7c4', '#d8e8c3', '#dce8c1', '#e0e9c0', '#e3e9be', '#e7e9bc', '#ebeabb', '#efeab9', '#f3ebb8', '#f7ebb6', '#fbecb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#feda85', '#fdd489', '#fdcf8c', '#fcc98f', '#fbc393', '#fabd96', '#fab89a', '#f9b29d', '#f8aca0', '#f7a6a4', '#f6a0a7', '#f69baa', '#f595ae',
            ],
            'autumn': [
                '#f48fb1', '#ec94b6', '#e499bb', '#db9ec1', '#d3a3c6', '#cba8cb', '#c3add0', '#bbb2d5', '#b2b6db', '#aabbe0', '#a2c0e5', '#9ac5ea', '#91caf0', '#89cff5',
            ],
            'winter': [
                '#81d4fa', '#84d4f4', '#86d4ee', '#89d4e8', '#8bd5e2', '#8ed5dc', '#90d5d6', '#93d5d0', '#96d5cb', '#98d5c5', '#9bd5bf', '#9dd6b9', '#a0d6b3', '#a2d6ad',
            ],
            'spring': [
                '#a5d6a7', '#abd7a4', '#b2d7a2', '#b8d89f', '#bfd99c', '#c5da9a', '#ccda97', '#d2db94', '#d8dc92', '#dfdc8f', '#e5dd8d', '#ecde8a', '#f2df87', '#f9df85',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecd54', '#fdc559', '#fcbc5d', '#fbb462', '#faac67', '#f9a46c', '#f89c70', '#f69375', '#f58b7a', '#f4837f', '#f37b84', '#f27288', '#f16a8d',
            ],
            'autumn': [
                '#f06292', '#e46999', '#d970a0', '#cd77a8', '#c27eaf', '#b685b6', '#ab8cbd', '#a092c4', '#9499cc', '#88a0d3', '#7da7da', '#72aee1', '#66b5e9', '#5abcf0',
            ],
            'winter': [
                '#4fc3f7', '#53c3ef', '#56c4e7', '#5ac4de', '#5dc4d6', '#61c4ce', '#64c5c6', '#68c5be', '#6cc5b5', '#6fc6ad', '#73c6a5', '#76c69d', '#7ac694', '#7dc78c',
            ],
            'spring': [
                '#81c784', '#8ac880', '#93c97c', '#9cca79', '#a5cb75', '#aecc71', '#b7cd6d', '#c0ce6a', '#c9cf66', '#d2d062', '#dbd15e', '#e4d25a', '#edd357', '#f6d453',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fec02e', '#fcb634', '#fbac3a', '#faa33f', '#f89945', '#f78f4b', '#f68551', '#f47b57', '#f3715d', '#f16763', '#f05e68', '#ef546e', '#ed4a74',
            ],
            'autumn': [
                '#ec407a', '#de4883', '#d0518c', '#c25995', '#b4629d', '#a66aa6', '#9873af', '#8b7bb8', '#7d83c1', '#6f8cca', '#6194d3', '#539ddb', '#45a5e4', '#37aeed',
            ],
            'winter': [
                '#29b6f6', '#2db6ec', '#32b7e2', '#36b7d8', '#3ab7ce', '#3fb8c4', '#43b8ba', '#48b8b0', '#4cb9a6', '#50b99c', '#55ba92', '#59ba88', '#5dba7e', '#62bb74',
            ],
            'spring': [
                '#66bb6a', '#71bc65', '#7cbd61', '#87be5c', '#92bf57', '#9dc052', '#a8c14e', '#b2c249', '#bdc444', '#c8c540', '#d3c63b', '#dec736', '#e9c831', '#f4c92d',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb50e', '#fcaa14', '#fa9e1b', '#f99221', '#f78728', '#f67b2e', '#f47035', '#f2643c', '#f15842', '#ef4d49', '#ee414f', '#ec3556', '#eb2a5c',
            ],
            'autumn': [
                '#e91e63', '#d9286d', '#c83278', '#b83c82', '#a7468c', '#975097', '#865aa1', '#7664ac', '#666db6', '#5577c0', '#4581cb', '#348bd5', '#2495df', '#139fea',
            ],
            'winter': [
                '#03a9f4', '#08a9e8', '#0daadd', '#13aad1', '#18abc5', '#1dabb9', '#22acae', '#28aca2', '#2dac96', '#32ad8b', '#37ad7f', '#3cae73', '#42ae67', '#47af5c',
            ],
            'spring': [
                '#4caf50', '#59b04b', '#66b246', '#72b340', '#7fb43b', '#8cb536', '#99b731', '#a6b82c', '#b2b926', '#bfbb21', '#ccbc1c', '#d9bd17', '#e5be11', '#f2c00c',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca807', '#f99d0e', '#f79215', '#f4881b', '#f17d22', '#ee7229', '#ec6730', '#e95c37', '#e6513e', '#e34645', '#e03c4b', '#de3152', '#db2659',
            ],
            'autumn': [
                '#d81b60', '#c9246a', '#ba2d73', '#aa367c', '#9b4086', '#8c4990', '#7d5299', '#6e5ba2', '#5e64ac', '#4f6db6', '#4076bf', '#3180c9', '#2189d2', '#1292dc',
            ],
            'winter': [
                '#039be5', '#089bda', '#0c9cce', '#119cc3', '#159cb8', '#1a9dad', '#1e9da1', '#239e96', '#289e8b', '#2c9e7f', '#319f74', '#359f69', '#3a9f5e', '#3ea052',
            ],
            'spring': [
                '#43a047', '#50a142', '#5ea33d', '#6ba438', '#79a533', '#86a72e', '#94a829', '#a1aa24', '#aeab1e', '#bcac19', '#c9ae14', '#d7af0f', '#e4b00a', '#f2b205',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fb9606', '#f68d0d', '#f28313', '#ee791a', '#e96f21', '#e56627', '#e05c2e', '#dc5234', '#d8493b', '#d33f41', '#cf3548', '#cb2b4e', '#c62255',
            ],
            'autumn': [
                '#c2185b', '#b42063', '#a7286c', '#993074', '#8b387d', '#7d4085', '#70488e', '#625096', '#54589e', '#4760a7', '#3968af', '#2b70b8', '#1d78c0', '#1080c9',
            ],
            'winter': [
                '#0288d1', '#0688c6', '#0a89bc', '#0e89b1', '#118aa6', '#158a9c', '#198b91', '#1d8b86', '#218b7c', '#258c71', '#298c67', '#2c8d5c', '#308d51', '#348e47',
            ],
            'spring': [
                '#388e3c', '#468f38', '#549133', '#63922f', '#71932b', '#7f9427', '#8d9622', '#9c971e', '#aa981a', '#b89a15', '#c69b11', '#d49c0d', '#e39d09', '#f19f04',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f98606', '#f37d0c', '#ed7513', '#e86c19', '#e2631f', '#dc5a25', '#d6522c', '#d04932', '#ca4038', '#c4373e', '#bf2e44', '#b9264b', '#b31d51',
            ],
            'autumn': [
                '#ad1457', '#a11b5e', '#952266', '#88296d', '#7c3074', '#70377b', '#643e83', '#58468a', '#4b4d91', '#3f5499', '#335ba0', '#2762a7', '#1a69ae', '#0e70b6',
            ],
            'winter': [
                '#0277bd', '#0577b3', '#0878a9', '#0b789f', '#0f7995', '#12798b', '#157a81', '#187a78', '#1b7a6e', '#1e7b64', '#217b5a', '#257c50', '#287c46', '#2b7d3c',
            ],
            'spring': [
                '#2e7d32', '#3d7e2e', '#4c802b', '#5b8127', '#6a8224', '#798320', '#88851d', '#968619', '#a58715', '#b48912', '#c38a0e', '#d28b0b', '#e18c07', '#f08e04',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f66806', '#ee610b', '#e65a11', '#dd5317', '#d44c1c', '#cc4522', '#c33f28', '#bb382d', '#b23133', '#aa2a38', '#a2233e', '#991c44', '#901549',
            ],
            'autumn': [
                '#880e4f', '#7e1354', '#75185a', '#6b1e5f', '#612365', '#58286a', '#4e2d70', '#443375', '#3b387a', '#313d80', '#284285', '#1e478b', '#144d90', '#0b5296',
            ],
            'winter': [
                '#01579b', '#035892', '#055889', '#075881', '#085978', '#0a5a6f', '#0c5a66', '#0e5a5e', '#105b55', '#125c4c', '#145c43', '#155d3a', '#175d32', '#195e29',
            ],
            'spring': [
                '#1b5e20', '#2b5f1e', '#3c601b', '#4c6219', '#5c6317', '#6c6415', '#7d6512', '#8d6610', '#9d680e', '#ae690b', '#be6a09', '#ce6b07', '#de6d05', '#ef6e02',
            ],
        },
    },
    SezimalInteger('22'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff7e2', '#fff5e2', '#fef4e3', '#fef3e4', '#fef1e5', '#fef0e5', '#feefe6', '#fdede7', '#fdece8', '#fdebe8', '#fde9e9', '#fde8ea', '#fce7eb', '#fce5eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f8e6ee', '#f7e7f0', '#f5e9f1', '#f3eaf2', '#f1ebf3', '#efecf4', '#eeedf6', '#eceef7', '#eaeff8', '#e8f0f9', '#e6f2fa', '#e5f3fc', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e1f5fd', '#e2f5fb', '#e2f5fa', '#e3f5f8', '#e3f5f7', '#e4f5f6', '#e4f5f4', '#e5f5f3', '#e5f5f1', '#e6f5f0', '#e6f5ef', '#e7f5ed', '#e7f5ec', '#e8f5ea',
            ],
            'spring': [
                '#e8f5e9', '#eaf5e8', '#ebf5e8', '#edf6e7', '#eef6e7', '#f0f6e6', '#f1f6e6', '#f3f6e5', '#f4f7e5', '#f6f7e4', '#f7f7e4', '#f9f7e3', '#faf7e3', '#fcf8e2', '#fdf8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#ffe9b5', '#fee5b7', '#fee2b9', '#fddfbb', '#fddcbd', '#fcd8bf', '#fcd5c1', '#fbd2c2', '#fbcfc4', '#facbc6', '#fac8c8', '#f9c5ca', '#f9c2cc', '#f8bece',
            ],
            'autumn': [
                '#f8bbd0', '#f3bed3', '#efc1d6', '#eac3d9', '#e6c6dc', '#e1c9df', '#dccce2', '#d8cfe5', '#d3d1e7', '#cfd4ea', '#cad7ed', '#c5daf0', '#c1ddf3', '#bcdff6', '#b8e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b4e5f9', '#b6e5f5', '#b7e5f2', '#b9e5ee', '#bae5eb', '#bbe5e8', '#bde5e4', '#bee6e1', '#c0e6dd', '#c1e6da', '#c2e6d7', '#c4e6d3', '#c5e6d0', '#c7e6cc',
            ],
            'spring': [
                '#c8e6c9', '#cce6c8', '#cfe7c6', '#d3e7c5', '#d7e8c3', '#dae8c2', '#dee8c0', '#e2e9bf', '#e5e9bd', '#e9eabc', '#edeaba', '#f0eab9', '#f4ebb7', '#f8ebb6', '#fbecb4',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fedb85', '#fed588', '#fdd08b', '#fcca8f', '#fbc592', '#fbc095', '#faba98', '#f9b59b', '#f8af9e', '#f8aaa1', '#f7a5a4', '#f69fa8', '#f59aab', '#f594ae',
            ],
            'autumn': [
                '#f48fb1', '#ec94b6', '#e598bb', '#dd9dc0', '#d5a1c4', '#cea6c9', '#c6abce', '#beafd3', '#b7b4d8', '#afb8dd', '#a7bde2', '#a0c2e7', '#98c6eb', '#90cbf0', '#89cff5',
            ],
            'winter': [
                '#81d4fa', '#83d4f4', '#86d4ef', '#88d4e9', '#8bd5e4', '#8dd5de', '#8fd5d9', '#92d5d3', '#94d5ce', '#97d5c8', '#99d5c3', '#9bd5bd', '#9ed6b8', '#a0d6b2', '#a3d6ad',
            ],
            'spring': [
                '#a5d6a7', '#abd7a5', '#b1d7a2', '#b7d8a0', '#bdd99d', '#c3d99b', '#c9da98', '#cfdb96', '#d5db93', '#dbdc91', '#e1dd8e', '#e7dd8c', '#edde89', '#f3df87', '#f9df84',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecd53', '#fdc658', '#fcbe5c', '#fbb661', '#faaf65', '#f9a76a', '#f89f6e', '#f79873', '#f69077', '#f5887c', '#f48180', '#f37985', '#f27189', '#f16a8e',
            ],
            'autumn': [
                '#f06292', '#e56899', '#db6f9f', '#d075a6', '#c57cad', '#ba82b4', '#b089ba', '#a58fc1', '#9a96c8', '#8f9ccf', '#85a3d5', '#7aa9dc', '#6fb0e3', '#64b6ea', '#5abdf0',
            ],
            'winter': [
                '#4fc3f7', '#52c3ef', '#56c4e8', '#59c4e0', '#5cc4d8', '#60c4d1', '#63c5c9', '#66c5c1', '#6ac5ba', '#6dc5b2', '#70c6aa', '#74c6a3', '#77c69b', '#7ac693', '#7ec78c',
            ],
            'spring': [
                '#81c784', '#89c880', '#92c97d', '#9aca79', '#a3cb76', '#abcc72', '#b3cd6f', '#bcce6b', '#c4ce68', '#cdcf64', '#d5d061', '#ddd15d', '#e6d25a', '#eed356', '#f7d453',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fec12d', '#fcb833', '#fbae38', '#faa53e', '#f99c43', '#f79349', '#f68a4e', '#f58054', '#f47759', '#f26e5f', '#f16564', '#f05c6a', '#ef526f', '#ed4975',
            ],
            'autumn': [
                '#ec407a', '#df4882', '#d2508b', '#c55893', '#b85f9b', '#ab67a3', '#9e6fac', '#9177b4', '#847fbc', '#7787c4', '#6a8fcd', '#5d97d5', '#509edd', '#43a6e5', '#36aeee',
            ],
            'winter': [
                '#29b6f6', '#2db6ed', '#31b7e3', '#35b7da', '#39b7d1', '#3db8c7', '#41b8be', '#45b8b5', '#4ab9ab', '#4eb9a2', '#52b999', '#56ba8f', '#5aba86', '#5eba7d', '#62bb73',
            ],
            'spring': [
                '#66bb6a', '#70bc66', '#7abd61', '#85be5d', '#8fbf58', '#99c054', '#a3c150', '#adc24b', '#b8c347', '#c2c442', '#ccc53e', '#d6c63a', '#e0c735', '#ebc831', '#f5c92c',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#feb60d', '#fcab13', '#fba019', '#f99620', '#f88b26', '#f6802c', '#f57532', '#f36a38', '#f25f3e', '#f05444', '#ef494a', '#ed3f51', '#ec3457', '#ea295d',
            ],
            'autumn': [
                '#e91e63', '#da276d', '#ca3176', '#bb3a80', '#ac438a', '#9c4c93', '#8d569d', '#7e5fa7', '#6e68b0', '#5f71ba', '#507bc4', '#4084cd', '#318dd7', '#2296e1', '#12a0ea',
            ],
            'winter': [
                '#03a9f4', '#08a9e9', '#0daade', '#12aad3', '#16abc8', '#1babbd', '#20abb2', '#25aca7', '#2aac9d', '#2fad92', '#34ad87', '#39ad7c', '#3dae71', '#42ae66', '#47af5b',
            ],
            'spring': [
                '#4caf50', '#58b04b', '#64b146', '#70b341', '#7cb43d', '#88b538', '#94b633', '#a0b72e', '#abb929', '#b7ba24', '#c3bb1f', '#cfbc1a', '#dbbd16', '#e7bf11', '#f3c00c',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca906', '#fa9f0d', '#f79513', '#f58a1a', '#f28020', '#ef7626', '#ed6c2d', '#ea6233', '#e8583a', '#e54e40', '#e24446', '#e0394d', '#dd2f53', '#db255a',
            ],
            'autumn': [
                '#d81b60', '#ca2469', '#bc2c72', '#ad357b', '#9f3d83', '#91468c', '#834e95', '#75579e', '#665fa7', '#5868b0', '#4a70b9', '#3c79c2', '#2e81ca', '#1f8ad3', '#1192dc',
            ],
            'winter': [
                '#039be5', '#079bda', '#0c9cd0', '#109cc5', '#149cbb', '#189db0', '#1d9da6', '#219d9b', '#259e91', '#299e86', '#2e9e7c', '#329f71', '#369f67', '#3a9f5c', '#3fa052',
            ],
            'spring': [
                '#43a047', '#50a142', '#5ca33e', '#69a439', '#75a534', '#82a62f', '#8ea82b', '#9ba926', '#a7aa21', '#b4ab1c', '#c0ad18', '#cdae13', '#d9af0e', '#e6b009', '#f2b205',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fb9706', '#f78e0c', '#f38512', '#ef7c18', '#eb731e', '#e76a24', '#e3612a', '#de5731', '#da4e37', '#d6453d', '#d23c43', '#ce3349', '#ca2a4f', '#c62155',
            ],
            'autumn': [
                '#c2185b', '#b51f63', '#a8276b', '#9c2e73', '#8f367a', '#823d82', '#75458a', '#684c92', '#5c549a', '#4f5ba2', '#4263aa', '#356ab2', '#2872b9', '#1c79c1', '#0f81c9',
            ],
            'winter': [
                '#0288d1', '#0688c7', '#0989bd', '#0d89b3', '#108aa9', '#148a9f', '#188a95', '#1b8b8b', '#1f8b82', '#228c78', '#268c6e', '#2a8c64', '#2d8d5a', '#318d50', '#348e46',
            ],
            'spring': [
                '#388e3c', '#458f38', '#539034', '#609230', '#6d932c', '#7a9428', '#889524', '#959620', '#a2981c', '#af9918', '#bd9a14', '#ca9b10', '#d79c0c', '#e49e08', '#f29f04',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#fa8706', '#f47f0c', '#ef7611', '#e96e17', '#e4661d', '#de5e23', '#d95629', '#d34d2e', '#ce4534', '#c83d3a', '#c33540', '#bd2d46', '#b8244b', '#b21c51',
            ],
            'autumn': [
                '#ad1457', '#a21b5e', '#962165', '#8b286b', '#7f2e72', '#743579', '#693c80', '#5d4287', '#52498d', '#464f94', '#3b569b', '#305da2', '#2463a9', '#196aaf', '#0d70b6',
            ],
            'winter': [
                '#0277bd', '#0577b4', '#0878aa', '#0b78a1', '#0e7998', '#11798f', '#147985', '#177a7c', '#197a73', '#1c7b6a', '#1f7b60', '#227b57', '#257c4e', '#287c45', '#2b7d3b',
            ],
            'spring': [
                '#2e7d32', '#3c7e2f', '#4a7f2b', '#588128', '#668225', '#748321', '#82841e', '#90851b', '#9d8717', '#ab8814', '#b98911', '#c78a0d', '#d58b0a', '#e38d07', '#f18e03',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f76905', '#ef620b', '#e75c10', '#df5515', '#d74f1a', '#cf4820', '#c74225', '#c03b2a', '#b8352f', '#b02e35', '#a8283a', '#a0213f', '#981b44', '#90144a',
            ],
            'autumn': [
                '#880e4f', '#7f1354', '#761859', '#6d1d5e', '#642163', '#5b2668', '#522b6d', '#493072', '#403578', '#373a7d', '#2e3f82', '#254487', '#1c488c', '#134d91', '#0a5296',
            ],
            'winter': [
                '#01579b', '#035793', '#04588b', '#065882', '#08597a', '#0a5972', '#0b5a6a', '#0d5a62', '#0f5b59', '#115b51', '#125c49', '#145c41', '#165d39', '#185d30', '#195e28',
            ],
            'spring': [
                '#1b5e20', '#2a5f1e', '#39601c', '#49611a', '#586317', '#676415', '#766513', '#856611', '#95670f', '#a4680d', '#b3690b', '#c26a09', '#d16c06', '#e16d04', '#f06e02',
            ],
        },
    },
    SezimalInteger('23'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff7e2', '#fff6e2', '#fef4e3', '#fef3e4', '#fef2e4', '#fef0e5', '#feefe6', '#feeee6', '#fdede7', '#fdece8', '#fdeae9', '#fde9e9', '#fde8ea', '#fce6eb', '#fce5eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f9e6ee', '#f7e7ef', '#f5e8f0', '#f4e9f2', '#f2eaf3', '#f0ebf4', '#eeecf5', '#edeef6', '#ebeff7', '#e9f0f8', '#e8f1fa', '#e6f2fb', '#e4f3fc', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e1f5fd', '#e2f5fb', '#e2f5fa', '#e3f5f9', '#e3f5f7', '#e4f5f6', '#e4f5f5', '#e4f5f3', '#e5f5f2', '#e5f5f1', '#e6f5f0', '#e6f5ee', '#e7f5ed', '#e7f5ec', '#e8f5ea',
            ],
            'spring': [
                '#e8f5e9', '#e9f5e8', '#ebf5e8', '#ecf6e8', '#eef6e7', '#eff6e6', '#f1f6e6', '#f2f6e5', '#f3f6e5', '#f5f7e4', '#f6f7e4', '#f8f7e3', '#f9f7e3', '#fbf7e2', '#fcf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#ffe9b5', '#fee6b7', '#fee3b8', '#fde0ba', '#fdddbc', '#fcdabe', '#fcd7c0', '#fcd3c2', '#fbd0c3', '#fbcdc5', '#facac7', '#fac7c9', '#f9c4cb', '#f9c1cc', '#f8bece',
            ],
            'autumn': [
                '#f8bbd0', '#f4bed3', '#efc0d6', '#ebc3d8', '#e7c5db', '#e2c8de', '#decbe0', '#dacde3', '#d5d0e6', '#d1d3e9', '#cdd5ec', '#c9d8ee', '#c4dbf1', '#c0ddf4', '#bce0f6', '#b7e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b4e5f9', '#b6e5f6', '#b7e5f2', '#b8e5ef', '#bae5ec', '#bbe5e9', '#bce5e6', '#bee6e2', '#bfe6df', '#c0e6dc', '#c1e6d9', '#c3e6d6', '#c4e6d3', '#c5e6cf', '#c7e6cc',
            ],
            'spring': [
                '#c8e6c9', '#cbe6c8', '#cfe7c6', '#d2e7c5', '#d6e8c3', '#d9e8c2', '#dde8c1', '#e0e9bf', '#e3e9be', '#e7e9bd', '#eaeabb', '#eeeaba', '#f1eab8', '#f5ebb7', '#f8ebb6', '#fcecb4',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fedb85', '#fed688', '#fdd18b', '#fccc8e', '#fcc791', '#fbc294', '#fabd97', '#fab89a', '#f9b29c', '#f8ad9f', '#f7a8a2', '#f7a3a5', '#f69ea8', '#f599ab', '#f594ae',
            ],
            'autumn': [
                '#f48fb1', '#ed93b6', '#e698ba', '#de9cbf', '#d7a0c3', '#d0a5c8', '#c9a9cc', '#c2add1', '#bbb2d5', '#b3b6da', '#acbadf', '#a5bee3', '#9ec3e8', '#97c7ec', '#8fcbf1', '#88d0f5',
            ],
            'winter': [
                '#81d4fa', '#83d4f5', '#86d4f0', '#88d4ea', '#8ad4e5', '#8cd5e0', '#8ed5db', '#91d5d6', '#93d5d0', '#95d5cb', '#98d5c6', '#9ad5c1', '#9cd6bc', '#9ed6b7', '#a0d6b1', '#a3d6ac',
            ],
            'spring': [
                '#a5d6a7', '#abd7a5', '#b0d7a2', '#b6d8a0', '#bcd89e', '#c1d99b', '#c7da99', '#ccda97', '#d2db94', '#d8dc92', '#dddc90', '#e3dd8e', '#e8de8b', '#eede89', '#f4df87', '#f9df84',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fece53', '#fdc757', '#fcbf5c', '#fbb860', '#fab164', '#f9aa68', '#f8a36c', '#f89c70', '#f79475', '#f68d79', '#f5867d', '#f47f81', '#f37885', '#f2708a', '#f1698e',
            ],
            'autumn': [
                '#f06292', '#e66898', '#dc6e9f', '#d274a5', '#c87aab', '#be80b2', '#b486b8', '#aa8cbe', '#a092c4', '#9599cb', '#8b9fd1', '#81a5d7', '#77abde', '#6db1e4', '#63b7ea', '#59bdf1',
            ],
            'winter': [
                '#4fc3f7', '#52c3f0', '#55c3e9', '#58c4e1', '#5cc4da', '#5fc4d3', '#62c4cc', '#65c5c5', '#68c5be', '#6bc5b6', '#6ec5af', '#71c6a8', '#74c6a1', '#78c69a', '#7bc692', '#7ec78b',
            ],
            'spring': [
                '#81c784', '#89c881', '#91c97d', '#99ca7a', '#a0cb77', '#a8cb73', '#b0cc70', '#b8cd6d', '#c0ce6a', '#c8cf66', '#d0d063', '#d8d160', '#e0d25c', '#e7d259', '#efd356', '#f7d452',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fec12d', '#fdb932', '#fbb037', '#faa83c', '#f99f42', '#f89647', '#f78e4c', '#f68551', '#f47c56', '#f3745b', '#f26b60', '#f16266', '#f05a6b', '#ee5170', '#ed4975',
            ],
            'autumn': [
                '#ec407a', '#e04782', '#d44f8a', '#c75691', '#bb5e99', '#af65a1', '#a36ca8', '#9774b0', '#8b7bb8', '#7e82c0', '#728ac8', '#6691cf', '#5a98d7', '#4ea0df', '#41a7e6', '#35afee',
            ],
            'winter': [
                '#29b6f6', '#2db6ed', '#31b7e4', '#34b7dc', '#38b7d3', '#3cb8ca', '#40b8c2', '#44b8b9', '#48b8b0', '#4bb9a7', '#4fb99e', '#53b996', '#57ba8d', '#5bba84', '#5eba7c', '#62bb73',
            ],
            'spring': [
                '#66bb6a', '#70bc66', '#79bd62', '#83be5e', '#8cbf5a', '#96c055', '#9fc151', '#a9c24d', '#b2c249', '#bcc345', '#c6c441', '#cfc53d', '#d9c638', '#e2c734', '#ecc830', '#f5c92c',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#feb70d', '#fcad12', '#fba218', '#fa981e', '#f88e24', '#f7842a', '#f57a2f', '#f47035', '#f3653b', '#f15b40', '#f05146', '#ee474c', '#ed3d52', '#ec3258', '#ea285d',
            ],
            'autumn': [
                '#e91e63', '#db276c', '#cc2f75', '#be387e', '#b04187', '#a14990', '#935299', '#845ba2', '#7664ac', '#686cb5', '#5975be', '#4b7ec7', '#3c86d0', '#2e8fd9', '#2098e2', '#11a0eb',
            ],
            'winter': [
                '#03a9f4', '#08a9ea', '#0caae0', '#11aad5', '#15abcb', '#1aabc1', '#1eabb6', '#23acac', '#28aca2', '#2cac98', '#31ad8e', '#35ad83', '#3aad79', '#3eae6f', '#43ae65', '#47af5a',
            ],
            'spring': [
                '#4caf50', '#57b04b', '#62b147', '#6eb242', '#79b33e', '#84b539', '#8fb635', '#9ab730', '#a6b82c', '#b1b927', '#bcba22', '#c7bb1e', '#d2bc19', '#ddbe15', '#e9bf10', '#f4c00c',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fdaa06', '#faa00c', '#f89612', '#f58d18', '#f3841e', '#f07a24', '#ee702a', '#ec6730', '#e95e36', '#e7543c', '#e44a42', '#e24148', '#df374e', '#dd2e54', '#da245a',
            ],
            'autumn': [
                '#d81b60', '#cb2368', '#bd2b71', '#b03379', '#a33b81', '#95438a', '#884b92', '#7b539a', '#6e5ba2', '#6063ab', '#536bb3', '#4673bb', '#387bc4', '#2b83cc', '#1e8bd4', '#1093dd',
            ],
            'winter': [
                '#039be5', '#079bdb', '#0b9cd1', '#0f9cc7', '#139cbe', '#179db4', '#1b9daa', '#1f9da0', '#239e96', '#279e8c', '#2b9e82', '#2f9e78', '#339f6e', '#379f65', '#3b9f5b', '#3fa051',
            ],
            'spring': [
                '#43a047', '#4fa143', '#5aa23e', '#66a43a', '#72a535', '#7ea631', '#8aa72c', '#95a828', '#a1aa24', '#adab1f', '#b8ac1b', '#c4ad16', '#d0ae12', '#dcaf0d', '#e8b109', '#f3b204',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fb9806', '#f78f0b', '#f48611', '#f07e17', '#ec761c', '#e86d22', '#e46428', '#e05c2e', '#dd5433', '#d94b39', '#d5423f', '#d13a44', '#cd324a', '#ca2950', '#c62055',
            ],
            'autumn': [
                '#c2185b', '#b61f62', '#aa266a', '#9e2d71', '#923478', '#863b80', '#7a4287', '#6e498f', '#625096', '#56579d', '#4a5ea5', '#3e65ac', '#326cb4', '#2673bb', '#1a7ac2', '#0e81ca',
            ],
            'winter': [
                '#0288d1', '#0588c8', '#0989be', '#0c89b5', '#108aac', '#138aa2', '#168a99', '#1a8b90', '#1d8b86', '#208b7d', '#248c74', '#278c6b', '#2a8c61', '#2e8d58', '#318d4f', '#358e45',
            ],
            'spring': [
                '#388e3c', '#448f38', '#519034', '#5d9131', '#6a922d', '#769429', '#839526', '#8f9622', '#9c971e', '#a8981a', '#b49916', '#c19a13', '#cd9c0f', '#da9d0b', '#e69e08', '#f39f04',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#fa8705', '#f5800b', '#f07810', '#eb7016', '#e5691b', '#e06121', '#db5926', '#d6522c', '#d14a31', '#cc4236', '#c73a3c', '#c23341', '#bc2b47', '#b7234c', '#b21c52',
            ],
            'autumn': [
                '#ad1457', '#a21a5d', '#982064', '#8d276a', '#822d70', '#783377', '#6d397d', '#623f84', '#58468a', '#4d4c90', '#425297', '#37589d', '#2d5ea4', '#2264aa', '#176bb0', '#0d71b7',
            ],
            'winter': [
                '#0277bd', '#0577b4', '#0878ac', '#0a78a3', '#0d789a', '#107992', '#127989', '#157a80', '#187a78', '#1b7a6f', '#1e7b66', '#207b5d', '#237b55', '#267c4c', '#287c43', '#2b7d3b',
            ],
            'spring': [
                '#2e7d32', '#3b7e2f', '#487f2c', '#558029', '#628226', '#6f8322', '#7c841f', '#89851c', '#968619', '#a48716', '#b18813', '#be8910', '#cb8a0c', '#d88c09', '#e58d06', '#f28e03',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f86905', '#f0630a', '#e95d0f', '#e15714', '#da5119', '#d24b1e', '#cb4523', '#c33f28', '#bc382c', '#b53231', '#ad2c36', '#a6263b', '#9e2040', '#971a45', '#8f144a',
            ],
            'autumn': [
                '#880e4f', '#801354', '#771759', '#6f1c5d', '#662062', '#5e2567', '#55296b', '#4d2e70', '#443375', '#3c377a', '#343c7e', '#2b4083', '#234588', '#1a498d', '#124e92', '#095296',
            ],
            'winter': [
                '#01579b', '#035793', '#04588c', '#065884', '#08597c', '#095975', '#0b5a6d', '#0c5a65', '#0e5a5e', '#105b56', '#115b4e', '#135c46', '#145c3f', '#165d37', '#185d2f', '#195e28',
            ],
            'spring': [
                '#1b5e20', '#295f1e', '#38601c', '#46611a', '#546218', '#626316', '#706414', '#7f6512', '#8d6610', '#9b680e', '#aa690c', '#b86a0a', '#c66b08', '#d46c06', '#e26d04', '#f16e02',
            ],
        },
    },
})

_WEEKS_SHADE_SEASON_GRAY_GRADATION = SezimalDictionary({
    SezimalInteger('14'): {
        '50': {
            'summer': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'autumn': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'winter': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'spring': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
        },
        '100': {
            'summer': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'autumn': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'winter': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'spring': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
        },
        '200': {
            'summer': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'autumn': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'winter': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'spring': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
        },
        '300': {
            'summer': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'autumn': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'winter': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'spring': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
        },
        '400': {
            'summer': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'autumn': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'winter': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'spring': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
        },
        '500': {
            'summer': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'autumn': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'winter': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'spring': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
        },
        '600': {
            'summer': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'autumn': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'winter': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'spring': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
        },
        '700': {
            'summer': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'autumn': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'winter': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'spring': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
        },
        '800': {
            'summer': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'autumn': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'winter': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'spring': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
        },
        '900': {
            'summer': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'autumn': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'winter': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'spring': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
        },
    },
    SezimalInteger('15'): {
        '50': {
            'summer': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'autumn': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'winter': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'spring': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
        },
        '100': {
            'summer': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'autumn': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'winter': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'spring': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
        },
        '200': {
            'summer': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'autumn': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'winter': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'spring': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
        },
        '300': {
            'summer': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'autumn': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'winter': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'spring': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
        },
        '400': {
            'summer': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'autumn': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'winter': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'spring': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
        },
        '500': {
            'summer': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'autumn': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'winter': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'spring': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
        },
        '600': {
            'summer': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'autumn': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'winter': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'spring': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
        },
        '700': {
            'summer': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'autumn': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'winter': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'spring': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
        },
        '800': {
            'summer': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'autumn': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'winter': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'spring': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
        },
        '900': {
            'summer': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'autumn': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'winter': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'spring': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
        },
    },
    SezimalInteger('20'): {
        '50': {
            'summer': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'autumn': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'winter': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'spring': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
        },
        '100': {
            'summer': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'autumn': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'winter': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'spring': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
        },
        '200': {
            'summer': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'autumn': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'winter': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'spring': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
        },
        '300': {
            'summer': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'autumn': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'winter': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'spring': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
        },
        '400': {
            'summer': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'autumn': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'winter': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'spring': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
        },
        '500': {
            'summer': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'autumn': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'winter': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'spring': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
        },
        '600': {
            'summer': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'autumn': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'winter': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'spring': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
        },
        '700': {
            'summer': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'autumn': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'winter': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'spring': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
        },
        '800': {
            'summer': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'autumn': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'winter': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'spring': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
        },
        '900': {
            'summer': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'autumn': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'winter': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'spring': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
        },
    },
    SezimalInteger('21'): {
        '50': {
            'summer': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'autumn': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'winter': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'spring': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
        },
        '100': {
            'summer': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'autumn': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'winter': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'spring': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
        },
        '200': {
            'summer': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'autumn': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'winter': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'spring': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
        },
        '300': {
            'summer': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'autumn': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'winter': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'spring': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
        },
        '400': {
            'summer': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'autumn': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'winter': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'spring': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
        },
        '500': {
            'summer': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'autumn': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'winter': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'spring': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
        },
        '600': {
            'summer': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'autumn': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'winter': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'spring': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
        },
        '700': {
            'summer': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'autumn': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'winter': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'spring': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
        },
        '800': {
            'summer': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'autumn': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'winter': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'spring': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
        },
        '900': {
            'summer': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'autumn': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'winter': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'spring': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
        },
    },
    SezimalInteger('22'): {
        '50': {
            'summer': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'autumn': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'winter': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'spring': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
        },
        '100': {
            'summer': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'autumn': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'winter': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'spring': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
        },
        '200': {
            'summer': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'autumn': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'winter': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'spring': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
        },
        '300': {
            'summer': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'autumn': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'winter': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'spring': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
        },
        '400': {
            'summer': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'autumn': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'winter': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'spring': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
        },
        '500': {
            'summer': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'autumn': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'winter': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'spring': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
        },
        '600': {
            'summer': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'autumn': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'winter': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'spring': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
        },
        '700': {
            'summer': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'autumn': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'winter': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'spring': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
        },
        '800': {
            'summer': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'autumn': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'winter': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'spring': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
        },
        '900': {
            'summer': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'autumn': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'winter': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'spring': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
        },
    },
    SezimalInteger('23'): {
        '50': {
            'summer': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'autumn': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'winter': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
            'spring': [
                '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa', '#fafafa',
            ],
        },
        '100': {
            'summer': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'autumn': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'winter': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
            'spring': [
                '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5', '#f5f5f5',
            ],
        },
        '200': {
            'summer': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'autumn': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'winter': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
            'spring': [
                '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee',
            ],
        },
        '300': {
            'summer': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'autumn': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'winter': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
            'spring': [
                '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0', '#e0e0e0',
            ],
        },
        '400': {
            'summer': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'autumn': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'winter': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
            'spring': [
                '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd', '#bdbdbd',
            ],
        },
        '500': {
            'summer': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'autumn': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'winter': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
            'spring': [
                '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e', '#9e9e9e',
            ],
        },
        '600': {
            'summer': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'autumn': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'winter': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
            'spring': [
                '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575', '#757575',
            ],
        },
        '700': {
            'summer': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'autumn': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'winter': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
            'spring': [
                '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161', '#616161',
            ],
        },
        '800': {
            'summer': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'autumn': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'winter': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
            'spring': [
                '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242', '#424242',
            ],
        },
        '900': {
            'summer': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'autumn': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'winter': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
            'spring': [
                '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121', '#212121',
            ],
        },
    },
})


def weekly_season_colors(year: SezimalInteger, hemisphere: str, time_zone: str | ZoneInfo = None, gray_scale: bool = False) -> dict[SezimalInteger | int, str, str]:
    if year < 212_513:
        year = 212_513

    if year > 213_511:
        year = 213_511

    cache_key = str(year)
    cache_key += '|' + hemisphere
    cache_key += '|' + time_zone

    if gray_scale:
        cache = _WEEKLY_SEASON_GRAY_CACHE
    else:
        cache = _WEEKLY_SEASON_COLOR_CACHE

    if cache_key in cache:
        return cache[cache_key]

    prior_december_solstice = list_sun_moon(year - 1, time_zone=time_zone, event='december_solstice')[0][0]
    march_equinox = list_sun_moon(year, time_zone=time_zone, event='march_equinox')[0][0]
    june_solstice = list_sun_moon(year, time_zone=time_zone, event='june_solstice')[0][0]
    september_equinox = list_sun_moon(year, time_zone=time_zone, event='september_equinox')[0][0]
    december_solstice = list_sun_moon(year, time_zone=time_zone, event='december_solstice')[0][0]
    next_march_equinox = list_sun_moon(year + 1, time_zone=time_zone, event='march_equinox')[0][0]

    prior_year = prior_december_solstice.replace(day=55).week_in_year - prior_december_solstice.week_in_year + 1
    first_december_length = prior_year
    first_december_length += march_equinox.week_in_year - 1

    march_length = june_solstice.week_in_year - march_equinox.week_in_year
    june_length = september_equinox.week_in_year - june_solstice.week_in_year
    september_length = december_solstice.week_in_year - september_equinox.week_in_year

    second_december_length = december_solstice.replace(day=55).week_in_year - december_solstice.week_in_year + 1
    next_year = next_march_equinox.week_in_year - 1
    second_december_length += next_year

    res = SezimalDictionary({})

    lengths = [first_december_length, march_length, june_length, september_length, second_december_length]
    starting_points = [int(prior_year.decimal), 0, 0, 0, 0]
    finishing_points = [None, None, None, None, int(next_year.decimal)]
    weeks_spans = [first_december_length - prior_year, march_length, june_length, september_length, second_december_length - next_year + 1]

    if hemisphere == 'N':
        seasons = ['winter', 'spring', 'summer', 'autumn', 'winter']
    else:
        seasons = ['summer', 'autumn', 'winter', 'spring', 'summer']

    week_number= SezimalInteger(1)

    for i in SezimalRange(5):
        season = seasons[i]
        season_length = lengths[i]
        starting_point = starting_points[i]
        finishing_point = finishing_points[i]
        weeks_span = weeks_spans[i]

        for j in SezimalRange(weeks_span):
            res[week_number] = SezimalDictionary({})

            for shade in _SHADES:
                if gray_scale:
                    res[week_number][shade] = \
                        _WEEKS_SHADE_SEASON_GRAY_GRADATION[season_length][shade][season][starting_point:finishing_point][j]
                else:
                    res[week_number][shade] = \
                        _WEEKS_SHADE_SEASON_COLOR_GRADATION[season_length][shade][season][starting_point:finishing_point][j]

            week_number += SezimalInteger(1)

    res['february'] = list_sun_moon(year, time_zone=time_zone, event='february_cross_quarter')[0][0]
    res['march'] = march_equinox

    res['may'] = list_sun_moon(year, time_zone=time_zone, event='may_cross_quarter')[0][0]
    res['june'] = june_solstice

    res['august'] = list_sun_moon(year, time_zone=time_zone, event='august_cross_quarter')[0][0]
    res['september'] = september_equinox

    res['november'] = list_sun_moon(year, time_zone=time_zone, event='november_cross_quarter')[0][0]
    res['december'] = december_solstice

    #
    # Moon phases
    #
    for month in SezimalRange(1, 21):
        res[f'moon_{str(month).zfill(2)}'] = []
        for moon_date, moon_type, moon_name in \
            list_sun_moon(year, month, time_zone=time_zone, only_moon=True, only_four=True):
            res[f'moon_{str(month).zfill(2)}'].append(moon_date)

    cache[cache_key] = res

    return res
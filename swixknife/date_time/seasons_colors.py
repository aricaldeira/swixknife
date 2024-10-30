
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
                '#fff8e1', '#fff6e2', '#fef4e3', '#fef3e4', '#fef1e5', '#feefe6', '#fdede7', '#fdebe8', '#fde9e9', '#fde8ea',
            ],
            'autumn': [
                '#fce4ec', '#fae6ee', '#f7e7ef', '#f5e9f1', '#f2eaf3', '#f0ecf4', '#ededf6', '#ebeff7', '#e8f0f9', '#e6f2fb', '#e3f3fc',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e4f6fa', '#e5f6f8', '#e7f6f6', '#e8f6f4', '#eaf7f3', '#ebf7f1', '#edf7ef', '#eef7ed', '#f0f8eb',
            ],
            'spring': [
                '#f1f8e9', '#f2f8e8', '#f4f8e8', '#f5f8e7', '#f6f8e6', '#f7f8e5', '#f9f8e5', '#faf8e4', '#fbf8e3', '#fcf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee8b6', '#fee3b8', '#fddfbb', '#fcdabe', '#fcd6c0', '#fbd1c3', '#fbcdc5', '#fac8c8', '#f9c4cb',
            ],
            'autumn': [
                '#f8bbd0', '#f2bfd4', '#ebc3d8', '#e5c6dc', '#dfcae0', '#d9cee4', '#d2d2e8', '#ccd6ec', '#c6daf0', '#c0ddf4', '#b9e1f8',
            ],
            'winter': [
                '#b3e5fc', '#b7e6f7', '#bae6f3', '#bee7ee', '#c2e8e9', '#c6e9e4', '#c9e9e0', '#cdeadb', '#d1ebd6', '#d5ecd1', '#d8eccd',
            ],
            'spring': [
                '#dcedc8', '#dfedc6', '#e2edc4', '#e6edc2', '#e9edc0', '#ecedbe', '#efecbd', '#f2ecbb', '#f5ecb9', '#f9ecb7', '#fcecb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fed986', '#fdd18b', '#fcca8f', '#fbc393', '#fabb97', '#f9b49c', '#f8aca0', '#f7a5a4', '#f69ea8',
            ],
            'autumn': [
                '#f48fb1', '#ea95b8', '#df9cbe', '#d5a2c5', '#caa8cc', '#c0aed2', '#b5b5d9', '#abbbdf', '#a0c1e6', '#96c7ed', '#8bcef3',
            ],
            'winter': [
                '#81d4fa', '#87d5f2', '#8dd6eb', '#94d8e3', '#9ad9db', '#a0dad3', '#a6dbcc', '#acdcc4', '#b2ddbc', '#b9dfb4', '#bfe0ad',
            ],
            'spring': [
                '#c5e1a5', '#cae1a2', '#d0e19f', '#d5e19b', '#dae198', '#dfe195', '#e5e092', '#eae08f', '#efe08c', '#f4e088', '#fae085',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecb55', '#fcc05b', '#fbb661', '#faab67', '#f8a16d', '#f79674', '#f58c7a', '#f48180', '#f37786',
            ],
            'autumn': [
                '#f06292', '#e16b9b', '#d374a4', '#c47cae', '#b585b7', '#a78ec0', '#9897c9', '#8aa0d2', '#7ba9db', '#6cb1e5', '#5ebaee',
            ],
            'winter': [
                '#4fc3f7', '#58c5ec', '#60c6e2', '#69c8d7', '#72cacc', '#7acbc1', '#83cdb7', '#8bceac', '#94d0a1', '#9dd296', '#a5d38c',
            ],
            'spring': [
                '#aed581', '#b5d57c', '#bdd578', '#c4d573', '#cbd56f', '#d3d56a', '#dad566', '#e2d561', '#e9d55d', '#f0d558', '#f8d554',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fdbd2f', '#fcb137', '#faa43e', '#f89846', '#f68b4d', '#f57f55', '#f3725c', '#f16664', '#ef596b',
            ],
            'autumn': [
                '#ec407a', '#da4b85', '#c95591', '#b7609c', '#a56ba7', '#9376b2', '#8280be', '#708bc9', '#5e96d4', '#4ca1df', '#3babeb',
            ],
            'winter': [
                '#29b6f6', '#33b8e9', '#3ebadc', '#48bcce', '#53bec1', '#5dc0b4', '#68c2a7', '#72c49a', '#7dc68d', '#87c87f', '#92ca72',
            ],
            'spring': [
                '#9ccc65', '#a5cc5f', '#aecc5a', '#b7cb54', '#c0cb4f', '#c9cb49', '#d2cb44', '#dbcb3e', '#e4cb39', '#edca33', '#f6ca2e',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb20f', '#fba318', '#f99520', '#f78628', '#f57731', '#f36839', '#f15942', '#ef4a4a', '#ed3c52',
            ],
            'autumn': [
                '#e91e63', '#d42b70', '#bf377d', '#aa448b', '#955198', '#805da5', '#6c6ab2', '#5776bf', '#4283cc', '#2d90da', '#189ce7',
            ],
            'winter': [
                '#03a9f4', '#0fabe5', '#1caed5', '#28b0c6', '#34b2b6', '#41b5a7', '#4db797', '#5aba88', '#66bc78', '#72be69', '#7fc159',
            ],
            'spring': [
                '#8bc34a', '#96c344', '#a0c33e', '#abc238', '#b5c232', '#c0c22c', '#cac225', '#d5c21f', '#dfc219', '#eac113', '#f4c10d',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fba509', '#f89711', '#f48a1a', '#f17c23', '#ed6e2c', '#ea6034', '#e6523d', '#e34446', '#df374f',
            ],
            'autumn': [
                '#d81b60', '#c5276c', '#b13278', '#9e3e84', '#8b4a90', '#77559c', '#6461a9', '#506cb5', '#3d78c1', '#2a84cd', '#168fd9',
            ],
            'winter': [
                '#039be5', '#0e9dd6', '#199fc7', '#24a2b9', '#2fa4aa', '#3aa69b', '#45a88c', '#50aa7d', '#5bac6e', '#66af60', '#71b151',
            ],
            'spring': [
                '#7cb342', '#88b33c', '#94b336', '#a0b330', '#acb32a', '#b8b324', '#c3b31e', '#cfb318', '#dbb312', '#e7b30c', '#f3b306',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#f99408', '#f48711', '#ee7b19', '#e96f21', '#e36229', '#de5632', '#d8493a', '#d33d42', '#cd314a',
            ],
            'autumn': [
                '#c2185b', '#b12266', '#9f2c70', '#8e377b', '#7c4186', '#6b4b91', '#59559b', '#485fa6', '#3669b1', '#2574bc', '#137ec6',
            ],
            'winter': [
                '#0288d1', '#0b8ac3', '#158cb5', '#1e8ea7', '#279099', '#30928b', '#3a957e', '#439770', '#4c9962', '#559b54', '#5f9d46',
            ],
            'spring': [
                '#689f38', '#769f33', '#839f2e', '#919f29', '#9f9f24', '#ad9f1f', '#baa019', '#c8a014', '#d6a00f', '#e4a00a', '#f1a005',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f88408', '#f07910', '#e96d18', '#e16220', '#da5728', '#d24c2f', '#cb4137', '#c3363f', '#bc2a47',
            ],
            'autumn': [
                '#ad1457', '#9d1d60', '#8e266a', '#7e2f73', '#6f387c', '#5f4185', '#504a8f', '#405398', '#315ca1', '#2165aa', '#126eb4',
            ],
            'winter': [
                '#0277bd', '#0a79b0', '#117ba3', '#197c96', '#207e89', '#28807c', '#2f8270', '#378463', '#3e8656', '#468749', '#4d893c',
            ],
            'spring': [
                '#558b2f', '#648b2b', '#748c26', '#838c22', '#938c1e', '#a28d1a', '#b28d15', '#c18e11', '#d18e0d', '#e08e09', '#f08f04',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f46607', '#e95d0e', '#df5516', '#d44c1d', '#c94324', '#be3a2b', '#b33132', '#a82839', '#9e2041',
            ],
            'autumn': [
                '#880e4f', '#7c1556', '#6f1b5d', '#632264', '#57296b', '#4b2f72', '#3e3678', '#323c7f', '#264386', '#1a4a8d', '#0d5094',
            ],
            'winter': [
                '#01579b', '#065990', '#0a5a84', '#0f5c79', '#135e6e', '#185f62', '#1c6157', '#21624b', '#256440', '#2a6635', '#2e6729',
            ],
            'spring': [
                '#33691e', '#466a1b', '#586a19', '#6b6b16', '#7d6b13', '#906c10', '#a26c0e', '#b56d0b', '#c76d08', '#da6e05', '#ec6e03',
            ],
        },
        'A100': {
            'summer': [
                '#ffe57f', '#ffdc83', '#ffd387', '#ffc98b', '#ffc08f', '#ffb793', '#ffae97', '#ffa59b', '#ff9c9f', '#ff92a3',
            ],
            'autumn': [
                '#ff80ab', '#f388b3', '#e890ba', '#dc98c2', '#d1a0ca', '#c5a8d1', '#bab0d9', '#aeb8e0', '#a3c0e8', '#97c8f0', '#8cd0f7',
            ],
            'winter': [
                '#80d8ff', '#87dcf5', '#8edfeb', '#95e3e1', '#9ce6d7', '#a3eacd', '#a9edc2', '#b0f1b8', '#b7f4ae', '#bef8a4', '#c5fb9a',
            ],
            'spring': [
                '#ccff90', '#d1fd8e', '#d5fa8d', '#daf88b', '#dff68a', '#e3f388', '#e8f187', '#ecee85', '#f1ec84', '#f6ea82', '#fae781',
            ],
        },
        'A200': {
            'summer': [
                '#ffd740', '#ffc946', '#ffbc4c', '#ffae52', '#ffa058', '#ff925e', '#ff8563', '#ff7769', '#ff696f', '#ff5b75',
            ],
            'autumn': [
                '#ff4081', '#ee4c8c', '#dc5898', '#cb64a3', '#ba70af', '#a87cba', '#9788c6', '#8594d1', '#74a0dd', '#63ace8', '#51b8f4',
            ],
            'winter': [
                '#40c4ff', '#4ac9f0', '#55cfe1', '#5fd4d2', '#69d9c3', '#74dfb4', '#7ee4a4', '#89ea95', '#93ef86', '#9df477', '#a8fa68',
            ],
            'spring': [
                '#b2ff59', '#b9fb57', '#c0f854', '#c7f452', '#cef050', '#d5ed4e', '#dce94b', '#e3e649', '#eae247', '#f1de45', '#f8db42',
            ],
        },
        'A400': {
            'summer': [
                '#ffc400', '#feb208', '#fda010', '#fc8f18', '#fb7d20', '#fa6b28', '#fa592f', '#f94737', '#f8353f', '#f72447',
            ],
            'autumn': [
                '#f50057', '#df1066', '#c82076', '#b23085', '#9c4094', '#8650a3', '#6f60b3', '#5970c2', '#4380d1', '#2d90e0', '#16a0f0',
            ],
            'winter': [
                '#00b0ff', '#0bb7e8', '#15bed1', '#20c6ba', '#2bcda3', '#36d48c', '#40db76', '#4be25f', '#56e948', '#61f131', '#6bf81a',
            ],
            'spring': [
                '#76ff03', '#82fa03', '#8ff402', '#9bef02', '#a8ea02', '#b4e402', '#c1df01', '#cdd901', '#dad401', '#e6cf01', '#f3c900',
            ],
        },
        'A700': {
            'summer': [
                '#ffab00', '#fa9d09', '#f48f12', '#ef811b', '#ea7324', '#e5652d', '#df5735', '#da493e', '#d53b47', '#d02d50',
            ],
            'autumn': [
                '#c51162', '#b31d6e', '#a1287b', '#8f3487', '#7d4093', '#6b4ba0', '#5a57ac', '#4862b9', '#366ec5', '#247ad1', '#1285de',
            ],
            'winter': [
                '#0091ea', '#0998d7', '#129fc4', '#1ba6b0', '#24ad9d', '#2db48a', '#37ba77', '#40c164', '#49c851', '#52cf3d', '#5bd62a',
            ],
            'spring': [
                '#64dd17', '#72d815', '#80d413', '#8ecf11', '#9ccb0f', '#aac60d', '#b9c20a', '#c7bd08', '#d5b906', '#e3b404', '#f1b002',
            ],
        },
    },
    SezimalInteger('15'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff6e2', '#fef5e3', '#fef3e4', '#fef1e5', '#fef0e6', '#feeee6', '#fdece7', '#fdebe8', '#fde9e9', '#fce7ea',
            ],
            'autumn': [
                '#fce4ec', '#fae5ee', '#f8e7ef', '#f5e8f0', '#f3eaf2', '#f1ebf3', '#eeecf5', '#eceef6', '#eaeff8', '#e8f1fa', '#e6f2fb', '#e3f4fc',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e4f6fb', '#e5f6f9', '#e6f6f7', '#e8f6f5', '#e9f6f3', '#eaf7f2', '#ecf7f0', '#edf7ee', '#eef8ec', '#f0f8eb',
            ],
            'spring': [
                '#f1f8e9', '#f2f8e8', '#f3f8e8', '#f4f8e7', '#f6f8e6', '#f7f8e6', '#f8f8e5', '#f9f8e4', '#faf8e4', '#fcf8e3', '#fdf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee8b5', '#fee4b8', '#fde0ba', '#fddcbd', '#fcd8bf', '#fcd3c2', '#fbcfc4', '#facbc6', '#fac7c9', '#f9c3cb',
            ],
            'autumn': [
                '#f8bbd0', '#f2bed4', '#ecc2d7', '#e7c5db', '#e1c9df', '#dbcce2', '#d5d0e6', '#d0d3ea', '#cad7ed', '#c4dbf1', '#bedef5', '#b9e2f8',
            ],
            'winter': [
                '#b3e5fc', '#b6e6f8', '#bae6f3', '#bde7ef', '#c1e8eb', '#c4e8e6', '#c8e9e2', '#cbeade', '#ceead9', '#d2ebd5', '#d5ecd1', '#d9eccc',
            ],
            'spring': [
                '#dcedc8', '#dfedc6', '#e2edc4', '#e5edc3', '#e8edc1', '#ebedbf', '#eeecbe', '#f0ecbc', '#f3ecba', '#f6ecb8', '#f9ecb6', '#fcecb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fed986', '#fdd38a', '#fccc8e', '#fbc592', '#fabe96', '#fab89a', '#f9b19d', '#f8aaa1', '#f7a3a5', '#f69ca9',
            ],
            'autumn': [
                '#f48fb1', '#ea95b7', '#e19bbd', '#d7a0c3', '#cea6c9', '#c4accf', '#bbb2d5', '#b1b7dc', '#a7bde2', '#9ec3e8', '#94c9ee', '#8bcef4',
            ],
            'winter': [
                '#81d4fa', '#87d5f3', '#8cd6ec', '#92d7e5', '#98d8de', '#9dd9d7', '#a3dbd0', '#a9dcc8', '#aeddc1', '#b4deba', '#badfb3', '#bfe0ac',
            ],
            'spring': [
                '#c5e1a5', '#cae1a2', '#cfe19f', '#d4e19c', '#d8e199', '#dde196', '#e2e093', '#e7e091', '#ece08e', '#f0e08b', '#f5e088', '#fae085',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecb55', '#fcc25a', '#fbb860', '#faaf65', '#f9a56b', '#f89c70', '#f69276', '#f5887c', '#f47f81', '#f27587',
            ],
            'autumn': [
                '#f06292', '#e36a9a', '#d572a3', '#c87aab', '#ba82b4', '#ad8abc', '#a092c4', '#929bcd', '#85a3d5', '#77abde', '#6ab3e6', '#5cbbef',
            ],
            'winter': [
                '#4fc3f7', '#57c4ed', '#5fc6e3', '#67c8da', '#6fc9d0', '#77cac6', '#7eccbc', '#86ceb2', '#8ecfa8', '#96d09e', '#9ed295', '#a6d38b',
            ],
            'spring': [
                '#aed581', '#b5d57d', '#bcd579', '#c2d574', '#c9d570', '#d0d56c', '#d6d568', '#ddd564', '#e4d560', '#ebd55c', '#f2d557', '#f8d553',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fdbe2f', '#fcb336', '#faa83c', '#f99c43', '#f7904a', '#f68551', '#f47a58', '#f26e5f', '#f16266', '#ef576c',
            ],
            'autumn': [
                '#ec407a', '#dc4a84', '#cc548f', '#bb5e99', '#ab67a3', '#9b71ae', '#8b7bb8', '#7a85c2', '#6a8fcd', '#5a98d7', '#4aa2e1', '#39acec',
            ],
            'winter': [
                '#29b6f6', '#33b8ea', '#3cbade', '#46bcd2', '#4fbdc6', '#59bfba', '#62c1ae', '#6cc3a1', '#76c595', '#7fc789', '#89c87d', '#92ca71',
            ],
            'spring': [
                '#9ccc65', '#a4cc60', '#accc5b', '#b5cc56', '#bdcb51', '#c5cb4c', '#cecb46', '#d6cb41', '#decb3c', '#e6cb37', '#eeca32', '#f7ca2d',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb30f', '#fba616', '#fa981e', '#f88b26', '#f67d2d', '#f47035', '#f2623d', '#f05444', '#ee474c', '#ed3954',
            ],
            'autumn': [
                '#e91e63', '#d62a6f', '#c3357b', '#b04187', '#9c4c93', '#89589f', '#7664ac', '#636fb8', '#507bc4', '#3c86d0', '#2992dc', '#169de8',
            ],
            'winter': [
                '#03a9f4', '#0eabe6', '#1aadd8', '#25b0ca', '#30b2bb', '#3cb4ad', '#47b69f', '#52b891', '#5eba83', '#69bc75', '#74bf66', '#80c158',
            ],
            'spring': [
                '#8bc34a', '#95c344', '#9ec33f', '#a8c239', '#b2c234', '#bbc22e', '#c5c229', '#cfc223', '#d8c21d', '#e2c218', '#ecc112', '#f5c10d',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca608', '#f99a10', '#f58d18', '#f28020', '#ef7428', '#ec6730', '#e85a38', '#e54e40', '#e24148', '#de3450',
            ],
            'autumn': [
                '#d81b60', '#c6266b', '#b43076', '#a33b81', '#91468c', '#7f5097', '#6e5ba2', '#5c66ae', '#4a70b9', '#387bc4', '#2686cf', '#1590da',
            ],
            'winter': [
                '#039be5', '#0d9dd7', '#179fca', '#21a1bc', '#2ba3af', '#35a5a1', '#40a794', '#4aa986', '#54ab78', '#5ead6b', '#68af5d', '#72b150',
            ],
            'spring': [
                '#7cb342', '#87b33d', '#92b337', '#9db332', '#a8b32c', '#b3b326', '#beb321', '#c8b31c', '#d3b316', '#deb310', '#e9b30b', '#f4b306',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fa9508', '#f5890f', '#f07e17', '#eb731e', '#e66726', '#e05c2e', '#db5135', '#d6453d', '#d13a44', '#cc2f4c',
            ],
            'autumn': [
                '#c2185b', '#b22165', '#a22b6f', '#923478', '#823d82', '#72478c', '#625096', '#5259a0', '#4263aa', '#326cb4', '#2275bd', '#127fc7',
            ],
            'winter': [
                '#0288d1', '#0a8ac4', '#138cb8', '#1c8eab', '#24909e', '#2d9291', '#359384', '#3e9578', '#46976b', '#4e995e', '#579b52', '#609d45',
            ],
            'spring': [
                '#689f38', '#759f33', '#819f2f', '#8e9f2a', '#9a9f25', '#a79f21', '#b3a01c', '#c0a017', '#cda013', '#d9a00e', '#e6a009', '#f2a005',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f88507', '#f17a0e', '#eb7016', '#e4661d', '#dd5c24', '#d6522c', '#cf4733', '#c83d3a', '#c23341', '#bb2849',
            ],
            'autumn': [
                '#ad1457', '#9f1c60', '#912468', '#822d70', '#743579', '#663d82', '#58468a', '#494e92', '#3b569b', '#2d5ea4', '#1e66ac', '#106fb4',
            ],
            'winter': [
                '#0277bd', '#0979b1', '#107aa5', '#177c9a', '#1e7e8e', '#257f82', '#2c8176', '#32836a', '#39845e', '#408652', '#478847', '#4e893b',
            ],
            'spring': [
                '#558b2f', '#638b2b', '#718c27', '#808c23', '#8e8c1f', '#9c8d1b', '#aa8d18', '#b88d14', '#c68e10', '#d48e0c', '#e38e08', '#f18f04',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f56707', '#eb5f0d', '#e15714', '#d74f1a', '#cd4721', '#c33f28', '#ba362e', '#b02e35', '#a6263b', '#9c1e42',
            ],
            'autumn': [
                '#880e4f', '#7d1455', '#721a5c', '#662062', '#5b2668', '#502c6f', '#443375', '#39397b', '#2e3f82', '#234588', '#174b8e', '#0c5195',
            ],
            'winter': [
                '#01579b', '#055891', '#095a86', '#0e5b7c', '#125d71', '#165e67', '#1a605c', '#1e6252', '#226348', '#27653d', '#2b6633', '#2f6828',
            ],
            'spring': [
                '#33691e', '#446a1b', '#556a19', '#666a16', '#776b14', '#886b11', '#996c0f', '#aa6d0c', '#bb6d0a', '#cc6e08', '#dd6e05', '#ee6e03',
            ],
        },
        'A100': {
            'summer': [
                '#ffe57f', '#ffdd83', '#ffd486', '#ffcc8a', '#ffc38e', '#ffbb91', '#ffb295', '#ffaa99', '#ffa29c', '#ff99a0', '#ff91a4',
            ],
            'autumn': [
                '#ff80ab', '#f487b2', '#ea8fb9', '#df96c0', '#d59dc7', '#caa5ce', '#c0acd5', '#b5b3dc', '#aabbe3', '#a0c2ea', '#95c9f1', '#8bd1f8',
            ],
            'winter': [
                '#80d8ff', '#86dbf6', '#8ddeec', '#93e2e3', '#99e5da', '#a0e8d1', '#a6ecc8', '#acefbe', '#b3f2b5', '#b9f5ac', '#bff8a2', '#c6fc99',
            ],
            'spring': [
                '#ccff90', '#d0fd8f', '#d4fb8d', '#d9f88c', '#ddf68a', '#e1f489', '#e6f288', '#eaf086', '#eeee85', '#f2ec83', '#f6e982', '#fbe780',
            ],
        },
        'A200': {
            'summer': [
                '#ffd740', '#ffca45', '#ffbe4b', '#ffb150', '#ffa556', '#ff985b', '#ff8c60', '#ff7f66', '#ff726b', '#ff6671', '#ff5976',
            ],
            'autumn': [
                '#ff4081', '#ef4b8b', '#df5696', '#cf61a0', '#bf6cab', '#af77b5', '#a082c0', '#908dcb', '#8098d5', '#70a3e0', '#60aeea', '#50b9f4',
            ],
            'winter': [
                '#40c4ff', '#4ac9f1', '#53cee3', '#5cd3d6', '#66d8c8', '#70ddba', '#79e2ac', '#82e69e', '#8ceb90', '#95f082', '#9ff575', '#a8fa67',
            ],
            'spring': [
                '#b2ff59', '#b8fc57', '#bff855', '#c5f553', '#ccf251', '#d2ee4f', '#d8eb4c', '#dfe84a', '#e5e448', '#ece146', '#f2de44', '#f9da42',
            ],
        },
        'A400': {
            'summer': [
                '#ffc400', '#feb407', '#fda30e', '#fc9316', '#fc831d', '#fb7224', '#fa622c', '#f95233', '#f8413a', '#f83141', '#f72149',
            ],
            'autumn': [
                '#f50057', '#e10f65', '#cc1d73', '#b82c81', '#a33b8f', '#8f499d', '#7a58ab', '#6667b9', '#5275c7', '#3d84d5', '#2993e3', '#14a1f1',
            ],
            'winter': [
                '#00b0ff', '#0ab7ea', '#14bdd5', '#1ec4c0', '#27caab', '#31d196', '#3bd881', '#45de6c', '#4fe557', '#58eb42', '#62f22d', '#6cf818',
            ],
            'spring': [
                '#76ff03', '#81fa03', '#8df502', '#98f002', '#a4eb02', '#afe602', '#bbe202', '#c6dd01', '#d1d801', '#ddd301', '#e8ce00', '#f4c900',
            ],
        },
        'A700': {
            'summer': [
                '#ffab00', '#fa9e08', '#f59110', '#f08418', '#ec7821', '#e76b29', '#e25e31', '#dd5139', '#d84441', '#d4384a', '#cf2b52',
            ],
            'autumn': [
                '#c51162', '#b51c6d', '#a42679', '#943184', '#833c8f', '#73469b', '#6251a6', '#525cb1', '#4266bd', '#3171c8', '#217cd3', '#1086df',
            ],
            'winter': [
                '#0091ea', '#0897d8', '#119ec7', '#19a4b5', '#21aaa4', '#2ab192', '#32b780', '#3abd6f', '#43c45d', '#4bca4c', '#53d03a', '#5cd729',
            ],
            'spring': [
                '#64dd17', '#71d915', '#7ed513', '#8bd011', '#98cc0f', '#a5c80d', '#b2c40c', '#bec00a', '#cbbc08', '#d8b806', '#e5b304', '#f2af02',
            ],
        },
    },
    SezimalInteger('20'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff6e2', '#fff5e3', '#fef3e4', '#fef2e4', '#fef0e5', '#feefe6', '#fdede7', '#fdece8', '#fdeae9', '#fde9e9', '#fce7ea',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f8e7ef', '#f6e8f0', '#f4e9f2', '#f2ebf3', '#f0ecf4', '#ededf6', '#ebeef7', '#e9f0f8', '#e7f1fa', '#e5f2fb', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e3f5fb', '#e5f6f9', '#e6f6f8', '#e7f6f6', '#e8f6f4', '#eaf7f3', '#ebf7f1', '#ecf7ef', '#edf7ee', '#eff8ec', '#f0f8eb',
            ],
            'spring': [
                '#f1f8e9', '#f2f8e8', '#f3f8e8', '#f4f8e7', '#f5f8e7', '#f6f8e6', '#f7f8e5', '#f9f8e5', '#faf8e4', '#fbf8e3', '#fcf8e3', '#fdf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee8b5', '#fee4b7', '#fde1ba', '#fdddbc', '#fcd9be', '#fcd5c0', '#fbd2c3', '#fbcec5', '#facac7', '#fac6c9', '#f9c3cc',
            ],
            'autumn': [
                '#f8bbd0', '#f3bed3', '#edc1d7', '#e8c5da', '#e3c8de', '#ddcbe1', '#d8cee4', '#d3d2e8', '#ced5eb', '#c8d8ee', '#c3dbf2', '#bedff5', '#b8e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b6e6f8', '#b9e6f4', '#bce7f0', '#c0e7ec', '#c3e8e8', '#c6e9e4', '#c9e9e0', '#cceadc', '#cfebd8', '#d3ebd4', '#d6ecd0', '#d9eccc',
            ],
            'spring': [
                '#dcedc8', '#dfedc6', '#e1edc5', '#e4edc3', '#e7edc2', '#e9edc0', '#ecedbe', '#efecbd', '#f2ecbb', '#f4ecb9', '#f7ecb8', '#faecb6', '#fcecb5',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#feda86', '#fdd489', '#fccd8d', '#fcc790', '#fbc194', '#fabb98', '#f9b49b', '#f8ae9f', '#f7a8a3', '#f7a2a6', '#f69baa',
            ],
            'autumn': [
                '#f48fb1', '#eb94b7', '#e29abc', '#d99fc2', '#d1a4c7', '#c8aacd', '#bfafd3', '#b6b4d8', '#adb9de', '#a4bfe4', '#9cc4e9', '#93c9ef', '#8acff4',
            ],
            'winter': [
                '#81d4fa', '#86d5f3', '#8bd6ed', '#91d7e6', '#96d8e0', '#9bd9d9', '#a0dad3', '#a6dbcc', '#abdcc6', '#b0ddbf', '#b5deb9', '#bbdfb2', '#c0e0ac',
            ],
            'spring': [
                '#c5e1a5', '#c9e1a2', '#cee1a0', '#d2e19d', '#d7e19a', '#dbe198', '#e0e195', '#e4e092', '#e9e08f', '#ede08d', '#f2e08a', '#f6e087', '#fbe085',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecc54', '#fdc359', '#fcba5e', '#fab264', '#f9a969', '#f8a06e', '#f79773', '#f68e78', '#f5857d', '#f37d83', '#f27488',
            ],
            'autumn': [
                '#f06292', '#e4699a', '#d771a2', '#cb78a9', '#be80b1', '#b287b9', '#a68fc1', '#9996c8', '#8d9ed0', '#81a5d8', '#74ade0', '#68b4e7', '#5bbcef',
            ],
            'winter': [
                '#4fc3f7', '#56c4ee', '#5ec6e5', '#65c7dc', '#6cc9d3', '#74caca', '#7bcbc1', '#82cdb7', '#89ceae', '#91cfa5', '#98d19c', '#9fd293', '#a7d48a',
            ],
            'spring': [
                '#aed581', '#b4d57d', '#bad579', '#c1d575', '#c7d572', '#cdd56e', '#d3d56a', '#dad566', '#e0d562', '#e6d55e', '#ecd55b', '#f3d557', '#f9d553',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#febf2e', '#fcb535', '#fbaa3b', '#f9a041', '#f89548', '#f68a4e', '#f58054', '#f3755a', '#f26a61', '#f06067', '#ef556d',
            ],
            'autumn': [
                '#ec407a', '#dd4984', '#ce528d', '#bf5b97', '#b064a0', '#a16daa', '#9276b3', '#8380bd', '#7489c6', '#6592d0', '#569bd9', '#47a4e3', '#38adec',
            ],
            'winter': [
                '#29b6f6', '#32b8eb', '#3bb9e0', '#44bbd5', '#4cbdc9', '#55bebe', '#5ec0b3', '#67c2a8', '#70c49d', '#79c592', '#81c786', '#8ac97b', '#93ca70',
            ],
            'spring': [
                '#9ccc65', '#a4cc60', '#abcc5c', '#b3cc57', '#bacb52', '#c2cb4e', '#cacb49', '#d1cb44', '#d9cb3f', '#e1cb3b', '#e8ca36', '#f0ca31', '#f7ca2d',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb40e', '#fca815', '#fa9b1c', '#f88f23', '#f7822a', '#f57631', '#f36939', '#f15d40', '#f05047', '#ee444e', '#ec3755',
            ],
            'autumn': [
                '#e91e63', '#d7296e', '#c63379', '#b43e84', '#a24990', '#91539b', '#7f5ea6', '#6d69b1', '#5b74bc', '#4a7ec7', '#3889d3', '#2694de', '#159ee9',
            ],
            'winter': [
                '#03a9f4', '#0dabe7', '#18adda', '#22afcd', '#2db1c0', '#37b3b3', '#42b5a6', '#4cb798', '#57b98b', '#61bb7e', '#6cbd71', '#76bf64', '#81c157',
            ],
            'spring': [
                '#8bc34a', '#94c345', '#9dc340', '#a6c33b', '#afc235', '#b8c230', '#c1c22b', '#c9c226', '#d2c221', '#dbc21c', '#e4c116', '#edc111', '#f6c10c',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca707', '#f99c0f', '#f69016', '#f3841e', '#f07925', '#ed6d2c', '#ea6134', '#e7553b', '#e44a42', '#e13e4a', '#de3251',
            ],
            'autumn': [
                '#d81b60', '#c8256a', '#b72f74', '#a7397f', '#964289', '#864c93', '#76569d', '#6560a8', '#556ab2', '#4574bc', '#347dc6', '#2487d1', '#1391db',
            ],
            'winter': [
                '#039be5', '#0c9dd8', '#169fcc', '#1fa1bf', '#28a2b3', '#32a4a6', '#3ba69a', '#44a88d', '#4daa81', '#57ac74', '#60ad68', '#69af5b', '#73b14f',
            ],
            'spring': [
                '#7cb342', '#86b33d', '#90b338', '#9ab333', '#a4b32e', '#aeb329', '#b8b324', '#c3b31e', '#cdb319', '#d7b314', '#e1b30f', '#ebb30a', '#f5b305',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fa9607', '#f68b0e', '#f18115', '#ec761c', '#e86c23', '#e3612a', '#de5731', '#d94c38', '#d5423f', '#d03746', '#cb2d4d',
            ],
            'autumn': [
                '#c2185b', '#b32164', '#a4296d', '#963276', '#873a7f', '#784388', '#694c91', '#5b549b', '#4c5da4', '#3d66ad', '#2e6eb6', '#2077bf', '#117fc8',
            ],
            'winter': [
                '#0288d1', '#0a8ac5', '#128cb9', '#1a8dae', '#218fa2', '#299196', '#31938a', '#39947f', '#419673', '#499867', '#509a5b', '#589b50', '#609d44',
            ],
            'spring': [
                '#689f38', '#749f34', '#7f9f2f', '#8b9f2b', '#969f27', '#a29f22', '#ae9f1e', '#b9a01a', '#c5a016', '#d1a011', '#dca00d', '#e8a009', '#f3a004',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f98607', '#f27c0d', '#ec7314', '#e6691b', '#df6021', '#d95628', '#d34d2f', '#cd4336', '#c63a3c', '#c03043', '#ba274a',
            ],
            'autumn': [
                '#ad1457', '#a01c5f', '#932367', '#862b6f', '#783276', '#6b3a7e', '#5e4286', '#51498e', '#445196', '#37599e', '#2960a5', '#1c68ad', '#0f6fb5',
            ],
            'winter': [
                '#0277bd', '#0879b2', '#0f7aa7', '#157c9c', '#1c7d91', '#227f86', '#28807b', '#2f8271', '#358366', '#3b855b', '#428650', '#488845', '#4f893a',
            ],
            'spring': [
                '#558b2f', '#628b2b', '#6f8c28', '#7c8c24', '#898c21', '#968d1d', '#a38d19', '#b18d16', '#be8d12', '#cb8e0e', '#d88e0b', '#e58e07', '#f28f04',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f66806', '#ed600c', '#e45912', '#da5118', '#d14a1e', '#c84224', '#bf3b2b', '#b63331', '#ad2c37', '#a3243d', '#9a1d43',
            ],
            'autumn': [
                '#880e4f', '#7e1455', '#73195b', '#691f61', '#5e2466', '#542a6c', '#4a3072', '#3f3578', '#353b7e', '#2b4184', '#204689', '#164c8f', '#0b5195',
            ],
            'winter': [
                '#01579b', '#055891', '#095a88', '#0d5b7e', '#105d75', '#145e6b', '#185f61', '#1c6158', '#20624e', '#246344', '#27653b', '#2b6631', '#2f6828',
            ],
            'spring': [
                '#33691e', '#43691c', '#526a19', '#626a17', '#726b15', '#816b12', '#916c10', '#a16c0e', '#b16d0c', '#c06d09', '#d06e07', '#e06e05', '#ef6f02',
            ],
        },
        'A100': {
            'summer': [
                '#ffe57f', '#ffdd82', '#ffd586', '#ffce89', '#ffc68d', '#ffbe90', '#ffb693', '#ffaf97', '#ffa79a', '#ff9f9d', '#ff97a1', '#ff90a4',
            ],
            'autumn': [
                '#ff80ab', '#f587b1', '#eb8eb8', '#e294be', '#d89bc5', '#cea2cb', '#c4a9d2', '#bbafd8', '#b1b6df', '#a7bde5', '#9dc4ec', '#94caf2', '#8ad1f9',
            ],
            'winter': [
                '#80d8ff', '#86dbf6', '#8cdeee', '#92e1e5', '#97e4dd', '#9de7d4', '#a3eacc', '#a9edc3', '#aff0bb', '#b5f3b2', '#baf6aa', '#c0f9a1', '#c6fc99',
            ],
            'spring': [
                '#ccff90', '#d0fd8f', '#d4fb8d', '#d8f98c', '#dcf78b', '#e0f589', '#e4f388', '#e7f187', '#ebef86', '#efed84', '#f3eb83', '#f7e982', '#fbe780',
            ],
        },
        'A200': {
            'summer': [
                '#ffd740', '#ffcb45', '#ffc04a', '#ffb44f', '#ffa954', '#ff9d59', '#ff915e', '#ff8663', '#ff7a68', '#ff6e6d', '#ff6372', '#ff5777',
            ],
            'autumn': [
                '#ff4081', '#f04a8b', '#e25494', '#d35e9e', '#c469a8', '#b673b1', '#a77dbb', '#9887c5', '#8991cf', '#7b9bd8', '#6ca6e2', '#5db0ec', '#4fbaf5',
            ],
            'winter': [
                '#40c4ff', '#49c9f2', '#52cde5', '#5ad2d9', '#63d6cc', '#6cdbbf', '#75dfb2', '#7de4a6', '#86e899', '#8fed8c', '#98f17f', '#a0f673', '#a9fa66',
            ],
            'spring': [
                '#b2ff59', '#b8fc57', '#bef955', '#c4f653', '#caf351', '#d0f04f', '#d6ed4d', '#dbe94c', '#e1e64a', '#e7e348', '#ede046', '#f3dd44', '#f9da42',
            ],
        },
        'A400': {
            'summer': [
                '#ffc400', '#feb507', '#fda60d', '#fd9714', '#fc881b', '#fb7921', '#fa6a28', '#fa5a2f', '#f94b36', '#f83c3c', '#f72d43', '#f71e4a',
            ],
            'autumn': [
                '#f50057', '#e20e64', '#cf1b71', '#bc297e', '#aa368b', '#974498', '#8451a5', '#715fb1', '#5e6cbe', '#4b7acb', '#3987d8', '#2695e5', '#13a2f2',
            ],
            'winter': [
                '#00b0ff', '#09b6ec', '#12bcd8', '#1bc2c5', '#24c8b1', '#2dce9e', '#36d48b', '#40db77', '#49e164', '#52e751', '#5bed3d', '#64f32a', '#6df916',
            ],
            'spring': [
                '#76ff03', '#81fa03', '#8bf603', '#96f102', '#a0ed02', '#abe802', '#b5e402', '#c0df01', '#cadb01', '#d5d601', '#dfd201', '#eacd00', '#f4c900',
            ],
        },
        'A700': {
            'summer': [
                '#ffab00', '#fb9f08', '#f6930f', '#f28717', '#ed7c1e', '#e97026', '#e4642d', '#e05835', '#db4c3c', '#d74044', '#d2354b', '#ce2953',
            ],
            'autumn': [
                '#c51162', '#b61b6c', '#a72577', '#982f81', '#88388c', '#794296', '#6a4ca1', '#5b56ab', '#4c60b6', '#3d6ac0', '#2d73cb', '#1e7dd5', '#0f87e0',
            ],
            'winter': [
                '#0091ea', '#0897da', '#0f9dca', '#17a3b9', '#1fa8a9', '#26ae99', '#2eb489', '#36ba78', '#3ec068', '#45c658', '#4dcb48', '#55d137', '#5cd727',
            ],
            'spring': [
                '#64dd17', '#70d915', '#7cd513', '#88d112', '#94ce10', '#a0ca0e', '#acc60c', '#b7c20b', '#c3be09', '#cfba07', '#dbb705', '#e7b304', '#f3af02',
            ],
        },
    },
    SezimalInteger('21'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff7e2', '#fff5e3', '#fef4e3', '#fef2e4', '#fef1e5', '#feefe6', '#feeee6', '#fdede7', '#fdebe8', '#fdeae9', '#fde8ea', '#fce7ea',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f8e6ef', '#f6e8f0', '#f4e9f1', '#f2eaf2', '#f0ebf4', '#eeecf5', '#edeef6', '#ebeff8', '#e9f0f9', '#e7f1fa', '#e5f3fb', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fc', '#e3f5fb', '#e4f6fa', '#e6f6f8', '#e7f6f6', '#e8f6f5', '#e9f6f3', '#eaf7f2', '#ebf7f0', '#ecf7ef', '#eef7ee', '#eff8ec', '#f0f8ea',
            ],
            'spring': [
                '#f1f8e9', '#f2f8e8', '#f3f8e8', '#f4f8e7', '#f5f8e7', '#f6f8e6', '#f7f8e6', '#f8f8e5', '#f9f8e4', '#faf8e4', '#fbf8e3', '#fcf8e3', '#fdf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#fee9b5', '#fee5b7', '#fee2b9', '#fddebb', '#fcdbbd', '#fcd7bf', '#fcd3c2', '#fbd0c4', '#faccc6', '#fac9c8', '#fac5ca', '#f9c2cc',
            ],
            'autumn': [
                '#f8bbd0', '#f3bed3', '#eec1d6', '#e9c4d9', '#e4c7dd', '#dfcae0', '#dacde3', '#d5d0e6', '#d1d3e9', '#ccd6ec', '#c7d9ef', '#c2dcf3', '#bddff6', '#b8e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b6e6f8', '#b9e6f5', '#bce7f1', '#bfe7ed', '#c2e8e9', '#c5e8e6', '#c8e9e2', '#caeade', '#cdeadb', '#d0ebd7', '#d3ebd3', '#d6eccf', '#d9eccc',
            ],
            'spring': [
                '#dcedc8', '#deedc6', '#e1edc5', '#e4edc4', '#e6edc2', '#e9edc0', '#ebedbf', '#eeecbe', '#f0ecbc', '#f2ecba', '#f5ecb9', '#f8ecb7', '#faecb6', '#fcecb4',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#feda85', '#fdd489', '#fdcf8c', '#fcc98f', '#fbc393', '#fabd96', '#fab89a', '#f9b29d', '#f8aca0', '#f7a6a4', '#f6a0a7', '#f69baa',
            ],
            'autumn': [
                '#f48fb1', '#ec94b6', '#e499bb', '#db9ec1', '#d3a3c6', '#cba8cb', '#c3add0', '#bbb2d5', '#b2b6db', '#aabbe0', '#a2c0e5', '#9ac5ea', '#91caf0', '#89cff5',
            ],
            'winter': [
                '#81d4fa', '#86d5f4', '#8bd6ee', '#90d7e8', '#94d8e2', '#99d9dc', '#9edad6', '#a3dbd0', '#a8dbc9', '#addcc3', '#b2ddbd', '#b6deb7', '#bbdfb1', '#c0e0ab',
            ],
            'spring': [
                '#c5e1a5', '#c9e1a3', '#cde1a0', '#d1e19d', '#d6e19b', '#dae198', '#dee196', '#e2e093', '#e6e091', '#eae08e', '#eee08c', '#f3e08a', '#f7e087', '#fbe084',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecd54', '#fdc559', '#fcbc5d', '#fbb462', '#faac67', '#f9a46c', '#f89c70', '#f69375', '#f58b7a', '#f4837f', '#f37b84', '#f27288',
            ],
            'autumn': [
                '#f06292', '#e46999', '#d970a0', '#cd77a8', '#c27eaf', '#b685b6', '#ab8cbd', '#a092c4', '#9499cc', '#88a0d3', '#7da7da', '#72aee1', '#66b5e9', '#5abcf0',
            ],
            'winter': [
                '#4fc3f7', '#56c4ef', '#5dc6e6', '#63c7de', '#6ac8d5', '#71c9cd', '#78cbc4', '#7eccbc', '#85cdb4', '#8ccfab', '#93d0a3', '#9ad19a', '#a0d292', '#a7d489',
            ],
            'spring': [
                '#aed581', '#b4d57d', '#bad57a', '#bfd576', '#c5d573', '#cbd56f', '#d1d56c', '#d6d568', '#dcd564', '#e2d561', '#e8d55d', '#eed55a', '#f3d556', '#f9d553',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fec02e', '#fcb634', '#fbac3a', '#faa33f', '#f89945', '#f78f4b', '#f68551', '#f47b57', '#f3715d', '#f16763', '#f05e68', '#ef546e',
            ],
            'autumn': [
                '#ec407a', '#de4883', '#d0518c', '#c25995', '#b4629d', '#a66aa6', '#9873af', '#8b7bb8', '#7d83c1', '#6f8cca', '#6194d3', '#539ddb', '#45a5e4', '#37aeed',
            ],
            'winter': [
                '#29b6f6', '#31b8ec', '#39b9e1', '#42bbd7', '#4abccd', '#52bec2', '#5abfb8', '#62c1ae', '#6bc3a3', '#73c499', '#7bc68e', '#83c784', '#8cc97a', '#94ca6f',
            ],
            'spring': [
                '#9ccc65', '#a3cc61', '#aacc5c', '#b1cc58', '#b8cb54', '#bfcb4f', '#c6cb4b', '#cecb46', '#d5cb42', '#dccb3e', '#e3cb39', '#eaca35', '#f1ca31', '#f8ca2c',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#fdb50e', '#fcaa14', '#fa9e1b', '#f99221', '#f78728', '#f67b2e', '#f47035', '#f2643c', '#f15842', '#ef4d49', '#ee414f', '#ec3556',
            ],
            'autumn': [
                '#e91e63', '#d9286d', '#c83278', '#b83c82', '#a7468c', '#975097', '#865aa1', '#7664ac', '#666db6', '#5577c0', '#4581cb', '#348bd5', '#2495df', '#139fea',
            ],
            'winter': [
                '#03a9f4', '#0dabe8', '#16addc', '#20afd0', '#2ab0c3', '#34b2b7', '#3db4ab', '#47b69f', '#51b893', '#5aba87', '#64bc7b', '#6ebd6e', '#78bf62', '#81c156',
            ],
            'spring': [
                '#8bc34a', '#93c345', '#9cc340', '#a4c33c', '#acc237', '#b4c232', '#bdc22d', '#c5c229', '#cdc224', '#d6c21f', '#dec21a', '#e6c115', '#eec111', '#f7c10c',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca807', '#f99d0e', '#f79215', '#f4881b', '#f17d22', '#ee7229', '#ec6730', '#e95c37', '#e6513e', '#e34645', '#e03c4b', '#de3152',
            ],
            'autumn': [
                '#d81b60', '#c9246a', '#ba2d73', '#aa367c', '#9b4086', '#8c4990', '#7d5299', '#6e5ba2', '#5e64ac', '#4f6db6', '#4076bf', '#3180c9', '#2189d2', '#1292dc',
            ],
            'winter': [
                '#039be5', '#0c9dd9', '#149ece', '#1da0c2', '#26a2b6', '#2ea4ab', '#37a59f', '#40a794', '#48a988', '#51aa7c', '#59ac71', '#62ae65', '#6bb059', '#73b14e',
            ],
            'spring': [
                '#7cb342', '#85b33d', '#8fb339', '#98b334', '#a1b32f', '#abb32a', '#b4b326', '#beb321', '#c7b31c', '#d0b318', '#dab313', '#e3b30e', '#ecb309', '#f6b305',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fb9606', '#f68d0d', '#f28313', '#ee791a', '#e96f21', '#e56627', '#e05c2e', '#dc5234', '#d8493b', '#d33f41', '#cf3548', '#cb2b4e',
            ],
            'autumn': [
                '#c2185b', '#b42063', '#a7286c', '#993074', '#8b387d', '#7d4085', '#70488e', '#625096', '#54589e', '#4760a7', '#3968af', '#2b70b8', '#1d78c0', '#1080c9',
            ],
            'winter': [
                '#0288d1', '#098ac6', '#118bbb', '#188db0', '#1f8fa5', '#26909a', '#2e928f', '#359384', '#3c957a', '#44976f', '#4b9864', '#529a59', '#599c4e', '#619d43',
            ],
            'spring': [
                '#689f38', '#739f34', '#7e9f30', '#889f2c', '#939f28', '#9e9f24', '#a99f20', '#b3a01c', '#bea018', '#c9a014', '#d4a010', '#dfa00c', '#e9a008', '#f4a004',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#f98606', '#f37d0c', '#ed7513', '#e86c19', '#e2631f', '#dc5a25', '#d6522c', '#d04932', '#ca4038', '#c4373e', '#bf2e44', '#b9264b',
            ],
            'autumn': [
                '#ad1457', '#a11b5e', '#952266', '#88296d', '#7c3074', '#70377b', '#643e83', '#58468a', '#4b4d91', '#3f5499', '#335ba0', '#2762a7', '#1a69ae', '#0e70b6',
            ],
            'winter': [
                '#0277bd', '#0878b3', '#0e7aa9', '#147b9f', '#1a7d94', '#207e8a', '#268080', '#2c8176', '#31826c', '#378462', '#3d8558', '#43874d', '#498843', '#4f8a39',
            ],
            'spring': [
                '#558b2f', '#618b2c', '#6d8c28', '#798c25', '#868c22', '#928c1e', '#9e8d1b', '#aa8d18', '#b68d14', '#c28e11', '#ce8e0d', '#db8e0a', '#e78e07', '#f38f03',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f66806', '#ee610b', '#e65a11', '#dd5317', '#d44c1c', '#cc4522', '#c33f28', '#bb382d', '#b23133', '#aa2a38', '#a2233e', '#991c44',
            ],
            'autumn': [
                '#880e4f', '#7e1354', '#75185a', '#6b1e5f', '#612365', '#58286a', '#4e2d70', '#443375', '#3b387a', '#313d80', '#284285', '#1e478b', '#144d90', '#0b5296',
            ],
            'winter': [
                '#01579b', '#055892', '#085a89', '#0c5b80', '#0f5c77', '#135d6e', '#165f65', '#1a605c', '#1e6154', '#21634b', '#256442', '#286539', '#2c6630', '#2f6827',
            ],
            'spring': [
                '#33691e', '#42691c', '#506a1a', '#5f6a18', '#6d6b15', '#7c6b13', '#8a6c11', '#996c0f', '#a86c0d', '#b66d0b', '#c56d09', '#d36e06', '#e26e04', '#f06f02',
            ],
        },
        'A100': {
            'summer': [
                '#ffe57f', '#ffde82', '#ffd785', '#ffcf88', '#ffc88c', '#ffc18f', '#ffba92', '#ffb295', '#ffab98', '#ffa49b', '#ff9d9e', '#ff96a2', '#ff8ea5',
            ],
            'autumn': [
                '#ff80ab', '#f686b1', '#ed8db7', '#e493bd', '#db99c3', '#d29fc9', '#c9a6cf', '#c0acd5', '#b6b2db', '#adb9e1', '#a4bfe7', '#9bc5ed', '#92cbf3', '#89d2f9',
            ],
            'winter': [
                '#80d8ff', '#85dbf7', '#8bdeef', '#90e0e7', '#96e3df', '#9be6d7', '#a1e9cf', '#a6ecc8', '#abeec0', '#b1f1b8', '#b6f4b0', '#bcf7a8', '#c1f9a0', '#c7fc98',
            ],
            'spring': [
                '#ccff90', '#d0fd8f', '#d3fb8e', '#d7f98c', '#dbf88b', '#def68a', '#e2f489', '#e6f288', '#e9f086', '#edee85', '#f0ec84', '#f4eb83', '#f8e981', '#fbe780',
            ],
        },
        'A200': {
            'summer': [
                '#ffd740', '#ffcc45', '#ffc149', '#ffb74e', '#ffac53', '#ffa157', '#ff965c', '#ff8c60', '#ff8165', '#ff766a', '#ff6b6e', '#ff6073', '#ff5678',
            ],
            'autumn': [
                '#ff4081', '#f1498a', '#e45393', '#d65c9c', '#c866a5', '#bb6fae', '#ad79b7', '#a082c0', '#928bc9', '#8495d2', '#779edb', '#69a8e4', '#5bb1ed', '#4ebbf6',
            ],
            'winter': [
                '#40c4ff', '#48c8f3', '#50cce7', '#58d1db', '#61d5d0', '#69d9c4', '#71ddb8', '#79e2ac', '#81e6a0', '#89ea94', '#91ee88', '#9af27d', '#a2f771', '#aafb65',
            ],
            'spring': [
                '#b2ff59', '#b8fc57', '#bdf955', '#c2f654', '#c8f452', '#cdf150', '#d3ee4e', '#d8eb4c', '#dee84b', '#e3e549', '#e9e247', '#eee045', '#f4dd44', '#fada42',
            ],
        },
        'A400': {
            'summer': [
                '#ffc400', '#feb606', '#fea80c', '#fd9a13', '#fc8c19', '#fb7e1f', '#fb7025', '#fa622c', '#f95432', '#f94638', '#f8383e', '#f72a44', '#f61c4b',
            ],
            'autumn': [
                '#f50057', '#e40d63', '#d2196f', '#c0267b', '#af3287', '#9d3f93', '#8c4b9f', '#7a58ab', '#6965b7', '#5771c3', '#467ecf', '#358adb', '#2397e7', '#11a3f3',
            ],
            'winter': [
                '#00b0ff', '#08b6ed', '#11bbdb', '#19c1c9', '#22c7b7', '#2acca5', '#33d293', '#3bd881', '#43dd6f', '#4ce35d', '#54e84b', '#5dee39', '#65f427', '#6ef915',
            ],
            'spring': [
                '#76ff03', '#80fb03', '#8af703', '#93f202', '#9dee02', '#a7ea02', '#b1e602', '#bbe202', '#c4dd01', '#ced901', '#d8d501', '#e2d101', '#ebcc00', '#f5c800',
            ],
        },
        'A700': {
            'summer': [
                '#ffab00', '#fba007', '#f7950e', '#f38a15', '#ee7f1c', '#ea7423', '#e6692a', '#e25e31', '#de5338', '#da483f', '#d63d46', '#d1324d', '#cd2754',
            ],
            'autumn': [
                '#c51162', '#b71a6c', '#a92375', '#9b2c7f', '#8d3689', '#7f3f93', '#71489c', '#6251a6', '#545ab0', '#4663b9', '#386cc3', '#2a76cd', '#1c7fd7', '#0e88e0',
            ],
            'winter': [
                '#0091ea', '#0796db', '#0e9ccc', '#15a1bd', '#1da7ae', '#24ac9f', '#2bb290', '#32b780', '#39bc71', '#40c262', '#47c753', '#4fcd44', '#56d235', '#5dd826',
            ],
            'spring': [
                '#64dd17', '#6fd915', '#7ad614', '#85d212', '#90cf10', '#9bcb0f', '#a6c80d', '#b2c40c', '#bdc00a', '#c8bd08', '#d3b907', '#deb605', '#e9b203', '#f4af02',
            ],
        },
    },
    SezimalInteger('22'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff7e2', '#fff5e2', '#fef4e3', '#fef3e4', '#fef1e5', '#fef0e5', '#feefe6', '#fdede7', '#fdece8', '#fdebe8', '#fde9e9', '#fde8ea', '#fce7eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f8e6ee', '#f7e7f0', '#f5e9f1', '#f3eaf2', '#f1ebf3', '#efecf4', '#eeedf6', '#eceef7', '#eaeff8', '#e8f0f9', '#e6f2fa', '#e5f3fc', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fd', '#e3f5fb', '#e4f6fa', '#e5f6f8', '#e6f6f7', '#e7f6f6', '#e8f6f4', '#eaf7f3', '#ebf7f1', '#ecf7f0', '#edf7ef', '#eef7ed', '#eff8ec', '#f0f8ea',
            ],
            'spring': [
                '#f1f8e9', '#f2f8e8', '#f3f8e8', '#f4f8e7', '#f5f8e7', '#f6f8e6', '#f7f8e6', '#f8f8e5', '#f8f8e5', '#f9f8e4', '#faf8e4', '#fbf8e3', '#fcf8e3', '#fdf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#ffe9b5', '#fee5b7', '#fee2b9', '#fddfbb', '#fddcbd', '#fcd8bf', '#fcd5c1', '#fbd2c2', '#fbcfc4', '#facbc6', '#fac8c8', '#f9c5ca', '#f9c2cc',
            ],
            'autumn': [
                '#f8bbd0', '#f3bed3', '#efc1d6', '#eac3d9', '#e6c6dc', '#e1c9df', '#dccce2', '#d8cfe5', '#d3d1e7', '#cfd4ea', '#cad7ed', '#c5daf0', '#c1ddf3', '#bcdff6', '#b8e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b6e6f9', '#b8e6f5', '#bbe7f2', '#bee7ee', '#c1e8eb', '#c3e8e7', '#c6e9e4', '#c9e9e0', '#cceadd', '#ceead9', '#d1ebd6', '#d4ebd2', '#d7eccf', '#d9eccb',
            ],
            'spring': [
                '#dcedc8', '#deedc7', '#e1edc5', '#e3edc4', '#e5edc2', '#e8edc1', '#eaedc0', '#ecedbe', '#efecbd', '#f1ecbb', '#f3ecba', '#f6ecb9', '#f8ecb7', '#faecb6', '#fdecb4',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fedb85', '#fed588', '#fdd08b', '#fcca8f', '#fbc592', '#fbc095', '#faba98', '#f9b59b', '#f8af9e', '#f8aaa1', '#f7a5a4', '#f69fa8', '#f59aab',
            ],
            'autumn': [
                '#f48fb1', '#ec94b6', '#e598bb', '#dd9dc0', '#d5a1c4', '#cea6c9', '#c6abce', '#beafd3', '#b7b4d8', '#afb8dd', '#a7bde2', '#a0c2e7', '#98c6eb', '#90cbf0', '#89cff5',
            ],
            'winter': [
                '#81d4fa', '#86d5f4', '#8ad6ef', '#8fd7e9', '#93d7e3', '#98d8de', '#9cd9d8', '#a1dad2', '#a5dbcd', '#aadcc7', '#aeddc1', '#b3debc', '#b7deb6', '#bcdfb0', '#c0e0ab',
            ],
            'spring': [
                '#c5e1a5', '#c9e1a3', '#cde1a0', '#d1e19e', '#d4e19c', '#d8e199', '#dce197', '#e0e195', '#e4e092', '#e8e090', '#ece08e', '#f0e08b', '#f3e089', '#f7e087', '#fbe084',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fecd53', '#fdc658', '#fcbe5c', '#fbb661', '#faaf65', '#f9a76a', '#f89f6e', '#f79873', '#f69077', '#f5887c', '#f48180', '#f37985', '#f27189',
            ],
            'autumn': [
                '#f06292', '#e56899', '#db6f9f', '#d075a6', '#c57cad', '#ba82b4', '#b089ba', '#a58fc1', '#9a96c8', '#8f9ccf', '#85a3d5', '#7aa9dc', '#6fb0e3', '#64b6ea', '#5abdf0',
            ],
            'winter': [
                '#4fc3f7', '#55c4ef', '#5cc5e7', '#62c7df', '#68c8d8', '#6fc9d0', '#75cac8', '#7bcbc0', '#82cdb8', '#88ceb0', '#8ecfa8', '#95d0a0', '#9bd199', '#a1d391', '#a8d489',
            ],
            'spring': [
                '#aed581', '#b3d57e', '#b9d57a', '#bed577', '#c4d574', '#c9d570', '#ced56d', '#d4d56a', '#d9d566', '#dfd563', '#e4d560', '#e9d55c', '#efd559', '#f4d556', '#fad552',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fec12d', '#fcb833', '#fbae38', '#faa53e', '#f99c43', '#f79349', '#f68a4e', '#f58054', '#f47759', '#f26e5f', '#f16564', '#f05c6a', '#ef526f',
            ],
            'autumn': [
                '#ec407a', '#df4882', '#d2508b', '#c55893', '#b85f9b', '#ab67a3', '#9e6fac', '#9177b4', '#847fbc', '#7787c4', '#6a8fcd', '#5d97d5', '#509edd', '#43a6e5', '#36aeee',
            ],
            'winter': [
                '#29b6f6', '#31b7ec', '#38b9e3', '#40bad9', '#48bccf', '#4fbdc6', '#57bfbc', '#5fc0b2', '#66c2a9', '#6ec39f', '#76c595', '#7dc68c', '#85c882', '#8dc978', '#94cb6f',
            ],
            'spring': [
                '#9ccc65', '#a3cc61', '#a9cc5d', '#b0cc59', '#b6cb55', '#bdcb51', '#c4cb4d', '#cacb49', '#d1cb44', '#d7cb40', '#decb3c', '#e5cb38', '#ebca34', '#f2ca30', '#f8ca2c',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#feb60d', '#fcab13', '#fba019', '#f99620', '#f88b26', '#f6802c', '#f57532', '#f36a38', '#f25f3e', '#f05444', '#ef494a', '#ed3f51', '#ec3457',
            ],
            'autumn': [
                '#e91e63', '#da276d', '#ca3176', '#bb3a80', '#ac438a', '#9c4c93', '#8d569d', '#7e5fa7', '#6e68b0', '#5f71ba', '#507bc4', '#4084cd', '#318dd7', '#2296e1', '#12a0ea',
            ],
            'winter': [
                '#03a9f4', '#0cabe9', '#15acdd', '#1eaed2', '#27b0c7', '#30b2bb', '#39b3b0', '#42b5a5', '#4cb799', '#55b98e', '#5eba83', '#67bc77', '#70be6c', '#79c061', '#82c155',
            ],
            'spring': [
                '#8bc34a', '#93c346', '#9ac341', '#a2c33d', '#aac238', '#b2c234', '#b9c22f', '#c1c22b', '#c9c226', '#d1c222', '#d8c21d', '#e0c219', '#e8c114', '#f0c110', '#f7c10b',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fca906', '#fa9f0d', '#f79513', '#f58a1a', '#f28020', '#ef7626', '#ed6c2d', '#ea6233', '#e8583a', '#e54e40', '#e24446', '#e0394d', '#dd2f53',
            ],
            'autumn': [
                '#d81b60', '#ca2469', '#bc2c72', '#ad357b', '#9f3d83', '#91468c', '#834e95', '#75579e', '#665fa7', '#5868b0', '#4a70b9', '#3c79c2', '#2e81ca', '#1f8ad3', '#1192dc',
            ],
            'winter': [
                '#039be5', '#0b9dda', '#139ecf', '#1ba0c4', '#23a1ba', '#2ba3af', '#33a5a4', '#3ba699', '#44a88e', '#4ca983', '#54ab78', '#5cad6d', '#64ae63', '#6cb058', '#74b14d',
            ],
            'spring': [
                '#7cb342', '#85b33e', '#8db339', '#96b335', '#9fb330', '#a8b32c', '#b0b328', '#b9b323', '#c2b31f', '#cbb31a', '#d3b316', '#dcb312', '#e5b30d', '#eeb309', '#f6b304',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fb9706', '#f78e0c', '#f38512', '#ef7c18', '#eb731e', '#e76a24', '#e3612a', '#de5731', '#da4e37', '#d6453d', '#d23c43', '#ce3349', '#ca2a4f',
            ],
            'autumn': [
                '#c2185b', '#b51f63', '#a8276b', '#9c2e73', '#8f367a', '#823d82', '#75458a', '#684c92', '#5c549a', '#4f5ba2', '#4263aa', '#356ab2', '#2872b9', '#1c79c1', '#0f81c9',
            ],
            'winter': [
                '#0288d1', '#098ac7', '#108bbd', '#168db2', '#1d8ea8', '#24909e', '#2b9194', '#32938a', '#38947f', '#3f9675', '#46976b', '#4d9961', '#549a57', '#5a9c4c', '#619d42',
            ],
            'spring': [
                '#689f38', '#729f34', '#7c9f31', '#869f2d', '#909f29', '#9a9f25', '#a49f22', '#ae9f1e', '#b9a01a', '#c3a016', '#cda013', '#d7a00f', '#e1a00b', '#eba007', '#f5a004',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#fa8706', '#f47f0c', '#ef7611', '#e96e17', '#e4661d', '#de5e23', '#d95629', '#d34d2e', '#ce4534', '#c83d3a', '#c33540', '#bd2d46', '#b8244b',
            ],
            'autumn': [
                '#ad1457', '#a21b5e', '#962165', '#8b286b', '#7f2e72', '#743579', '#693c80', '#5d4287', '#52498d', '#464f94', '#3b569b', '#305da2', '#2463a9', '#196aaf', '#0d70b6',
            ],
            'winter': [
                '#0277bd', '#0878b4', '#0d7aaa', '#137ba1', '#187c97', '#1e7e8e', '#237f84', '#29807b', '#2e8271', '#348368', '#39845e', '#3f8655', '#44874b', '#4a8842', '#4f8a38',
            ],
            'spring': [
                '#558b2f', '#608b2c', '#6c8c29', '#778c26', '#828c22', '#8e8c1f', '#998d1c', '#a48d19', '#b08d16', '#bb8d13', '#c68e10', '#d28e0d', '#dd8e09', '#e88e06', '#f48f03',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f76905', '#ef620b', '#e75c10', '#df5515', '#d74f1a', '#cf4820', '#c74225', '#c03b2a', '#b8352f', '#b02e35', '#a8283a', '#a0213f', '#981b44',
            ],
            'autumn': [
                '#880e4f', '#7f1354', '#761859', '#6d1d5e', '#642163', '#5b2668', '#522b6d', '#493072', '#403578', '#373a7d', '#2e3f82', '#254487', '#1c488c', '#134d91', '#0a5296',
            ],
            'winter': [
                '#01579b', '#045893', '#08598a', '#0b5b82', '#0e5c7a', '#125d71', '#155e69', '#185f61', '#1c6158', '#1f6250', '#226348', '#26643f', '#296537', '#2c672f', '#306826',
            ],
            'spring': [
                '#33691e', '#41691c', '#4e6a1a', '#5c6a18', '#696b16', '#776b14', '#856b12', '#926c10', '#a06c0e', '#ad6d0c', '#bb6d0a', '#c96d08', '#d66e06', '#e46e04', '#f16f02',
            ],
        },
        'A100': {
            'summer': [
                '#ffe57f', '#ffde82', '#ffd885', '#ffd188', '#ffca8b', '#ffc38e', '#ffbd91', '#ffb694', '#ffaf96', '#ffa899', '#ffa29c', '#ff9b9f', '#ff94a2', '#ff8da5',
            ],
            'autumn': [
                '#ff80ab', '#f786b1', '#ee8cb6', '#e692bc', '#dd97c1', '#d59dc7', '#cca3cd', '#c4a9d2', '#bbafd8', '#b3b5dd', '#aabbe3', '#a2c1e9', '#99c6ee', '#91ccf4', '#88d2f9',
            ],
            'winter': [
                '#80d8ff', '#85dbf8', '#8addf0', '#8fe0e9', '#94e2e1', '#99e5da', '#9ee8d3', '#a3eacb', '#a9edc4', '#aeefbc', '#b3f2b5', '#b8f5ae', '#bdf7a6', '#c2fa9f', '#c7fc97',
            ],
            'spring': [
                '#ccff90', '#cffd8f', '#d3fc8e', '#d6fa8d', '#daf88b', '#ddf68a', '#e0f589', '#e4f388', '#e7f187', '#ebef86', '#eeee85', '#f1ec84', '#f5ea82', '#f8e881', '#fce780',
            ],
        },
        'A200': {
            'summer': [
                '#ffd740', '#ffcd44', '#ffc349', '#ffb94d', '#ffaf51', '#ffa556', '#ff9b5a', '#ff915e', '#ff8663', '#ff7c67', '#ff726b', '#ff6870', '#ff5e74', '#ff5478',
            ],
            'autumn': [
                '#ff4081', '#f24989', '#e65292', '#d95a9a', '#cc63a3', '#bf6cab', '#b375b3', '#a67ebc', '#9986c4', '#8c8fcd', '#8098d5', '#73a1dd', '#66aae6', '#59b2ee', '#4dbbf7',
            ],
            'winter': [
                '#40c4ff', '#48c8f4', '#4fcce9', '#57d0de', '#5ed4d3', '#66d8c8', '#6edcbd', '#75e0b2', '#7de3a6', '#84e79b', '#8ceb90', '#94ef85', '#9bf37a', '#a3f76f', '#aafb64',
            ],
            'spring': [
                '#b2ff59', '#b7fc57', '#bcfa56', '#c1f754', '#c7f452', '#ccf251', '#d1ef4f', '#d6ec4d', '#dbea4c', '#e0e74a', '#e5e448', '#eae247', '#f0df45', '#f5dc43', '#fada42',
            ],
        },
        'A400': {
            'summer': [
                '#ffc400', '#feb706', '#feaa0c', '#fd9d11', '#fc9017', '#fc831d', '#fb7623', '#fa6929', '#fa5b2e', '#f94e34', '#f8413a', '#f83440', '#f72746', '#f61a4b',
            ],
            'autumn': [
                '#f50057', '#e50c62', '#d4176d', '#c42379', '#b42f84', '#a33b8f', '#93469a', '#8352a5', '#725eb1', '#626abc', '#5275c7', '#4181d2', '#318ddd', '#2199e9', '#10a4f4',
            ],
            'winter': [
                '#00b0ff', '#08b5ee', '#10bbdd', '#18c0cd', '#1fc5bc', '#27caab', '#2fd09a', '#37d589', '#3fda79', '#47df68', '#4fe557', '#57ea46', '#5eef35', '#66f425', '#6efa14',
            ],
            'spring': [
                '#76ff03', '#7ffb03', '#88f703', '#91f302', '#9bef02', '#a4eb02', '#ade702', '#b6e302', '#bfe001', '#c8dc01', '#d1d801', '#dad401', '#e4d001', '#edcc00', '#f6c800',
            ],
        },
        'A700': {
            'summer': [
                '#ffab00', '#fba107', '#f7960d', '#f38c14', '#f0821a', '#ec7821', '#e86d27', '#e4632e', '#e05934', '#dc4f3b', '#d84441', '#d43a48', '#d1304e', '#cd2655',
            ],
            'autumn': [
                '#c51162', '#b81a6b', '#ab2274', '#9e2b7d', '#903386', '#833c8f', '#764498', '#694da1', '#5c55ab', '#4f5eb4', '#4266bd', '#356fc6', '#2777cf', '#1a80d8', '#0d88e1',
            ],
            'winter': [
                '#0091ea', '#0796dc', '#0d9bce', '#14a0c0', '#1ba5b2', '#21aaa4', '#28af96', '#2fb488', '#35ba79', '#3cbf6b', '#43c45d', '#49c94f', '#50ce41', '#57d333', '#5dd825',
            ],
            'spring': [
                '#64dd17', '#6eda15', '#79d614', '#83d312', '#8dd011', '#98cc0f', '#a2c90e', '#acc60c', '#b7c20b', '#c1bf09', '#cbbc08', '#d6b806', '#e0b505', '#eab203', '#f5ae02',
            ],
        },
    },
    SezimalInteger('23'): {
        '50': {
            'summer': [
                '#fff8e1', '#fff7e2', '#fff6e2', '#fef4e3', '#fef3e4', '#fef2e4', '#fef0e5', '#feefe6', '#feeee6', '#fdede7', '#fdece8', '#fdeae9', '#fde9e9', '#fde8ea', '#fce6eb',
            ],
            'autumn': [
                '#fce4ec', '#fae5ed', '#f9e6ee', '#f7e7ef', '#f5e8f0', '#f4e9f2', '#f2eaf3', '#f0ebf4', '#eeecf5', '#edeef6', '#ebeff7', '#e9f0f8', '#e8f1fa', '#e6f2fb', '#e4f3fc', '#e3f4fd',
            ],
            'winter': [
                '#e1f5fe', '#e2f5fd', '#e3f5fb', '#e4f6fa', '#e5f6f9', '#e6f6f7', '#e7f6f6', '#e8f6f5', '#e9f6f3', '#eaf7f2', '#ebf7f1', '#ecf7f0', '#edf7ee', '#eef7ed', '#eff8ec', '#f0f8ea',
            ],
            'spring': [
                '#f1f8e9', '#f2f8e8', '#f3f8e8', '#f4f8e8', '#f4f8e7', '#f5f8e6', '#f6f8e6', '#f7f8e5', '#f8f8e5', '#f9f8e4', '#faf8e4', '#fbf8e3', '#fcf8e3', '#fcf8e2', '#fdf8e2', '#fef8e2',
            ],
        },
        '100': {
            'summer': [
                '#ffecb3', '#ffe9b5', '#fee6b7', '#fee3b8', '#fde0ba', '#fdddbc', '#fcdabe', '#fcd7c0', '#fcd3c2', '#fbd0c3', '#fbcdc5', '#facac7', '#fac7c9', '#f9c4cb', '#f9c1cc',
            ],
            'autumn': [
                '#f8bbd0', '#f4bed3', '#efc0d6', '#ebc3d8', '#e7c5db', '#e2c8de', '#decbe0', '#dacde3', '#d5d0e6', '#d1d3e9', '#cdd5ec', '#c9d8ee', '#c4dbf1', '#c0ddf4', '#bce0f6', '#b7e2f9',
            ],
            'winter': [
                '#b3e5fc', '#b6e6f9', '#b8e6f6', '#bbe7f2', '#bde7ef', '#c0e8ec', '#c2e8e9', '#c5e8e5', '#c8e9e2', '#caeadf', '#cdeadc', '#cfebd8', '#d2ebd5', '#d4ecd2', '#d7ecce', '#d9eccb',
            ],
            'spring': [
                '#dcedc8', '#deedc7', '#e0edc5', '#e3edc4', '#e5edc3', '#e7edc1', '#e9edc0', '#ebedbf', '#eeecbe', '#f0ecbc', '#f2ecbb', '#f4ecba', '#f6ecb8', '#f8ecb7', '#fbecb6', '#fdecb4',
            ],
        },
        '200': {
            'summer': [
                '#ffe082', '#fedb85', '#fed688', '#fdd18b', '#fccc8e', '#fcc791', '#fbc294', '#fabd97', '#fab89a', '#f9b29c', '#f8ad9f', '#f7a8a2', '#f7a3a5', '#f69ea8', '#f599ab',
            ],
            'autumn': [
                '#f48fb1', '#ed93b6', '#e698ba', '#de9cbf', '#d7a0c3', '#d0a5c8', '#c9a9cc', '#c2add1', '#bbb2d5', '#b3b6da', '#acbadf', '#a5bee3', '#9ec3e8', '#97c7ec', '#8fcbf1', '#88d0f5',
            ],
            'winter': [
                '#81d4fa', '#85d5f5', '#8ad6ef', '#8ed6ea', '#92d7e5', '#96d8df', '#9bd9da', '#9fdad5', '#a3dbd0', '#a7dbca', '#acdcc5', '#b0ddc0', '#b4deba', '#b8dfb5', '#bcdfb0', '#c1e0aa',
            ],
            'spring': [
                '#c5e1a5', '#c9e1a3', '#cce1a1', '#d0e19e', '#d4e19c', '#d7e19a', '#dbe198', '#dee196', '#e2e093', '#e6e091', '#e9e08f', '#ede08d', '#f0e08b', '#f4e089', '#f8e086', '#fbe084',
            ],
        },
        '300': {
            'summer': [
                '#ffd54f', '#fece53', '#fdc757', '#fcbf5c', '#fbb860', '#fab164', '#f9aa68', '#f8a36c', '#f89c70', '#f79475', '#f68d79', '#f5867d', '#f47f81', '#f37885', '#f2708a',
            ],
            'autumn': [
                '#f06292', '#e66898', '#dc6e9f', '#d274a5', '#c87aab', '#be80b2', '#b486b8', '#aa8cbe', '#a092c4', '#9599cb', '#8b9fd1', '#81a5d7', '#77abde', '#6db1e4', '#63b7ea', '#59bdf1',
            ],
            'winter': [
                '#4fc3f7', '#55c4f0', '#5bc5e8', '#61c6e1', '#67c8da', '#6dc9d2', '#73cacb', '#79cbc3', '#7eccbc', '#84cdb5', '#8acead', '#90cfa6', '#96d09e', '#9cd297', '#a2d390', '#a8d488',
            ],
            'spring': [
                '#aed581', '#b3d57e', '#b8d57b', '#bdd578', '#c2d574', '#c7d571', '#ccd56e', '#d1d56b', '#d6d568', '#dcd565', '#e1d562', '#e6d55f', '#ebd55c', '#f0d558', '#f5d555', '#fad552',
            ],
        },
        '400': {
            'summer': [
                '#ffca28', '#fec12d', '#fdb932', '#fbb037', '#faa83c', '#f99f42', '#f89647', '#f78e4c', '#f68551', '#f47c56', '#f3745b', '#f26b60', '#f16266', '#f05a6b', '#ee5170',
            ],
            'autumn': [
                '#ec407a', '#e04782', '#d44f8a', '#c75691', '#bb5e99', '#af65a1', '#a36ca8', '#9774b0', '#8b7bb8', '#7e82c0', '#728ac8', '#6691cf', '#5a98d7', '#4ea0df', '#41a7e6', '#35afee',
            ],
            'winter': [
                '#29b6f6', '#30b7ed', '#37b9e4', '#3fbadb', '#46bcd2', '#4dbdc9', '#54bec0', '#5bc0b7', '#62c1ae', '#6ac2a4', '#71c49b', '#78c592', '#7fc789', '#86c880', '#8ec977', '#95cb6e',
            ],
            'spring': [
                '#9ccc65', '#a2cc61', '#a8cc5d', '#afcc5a', '#b5cc56', '#bbcb52', '#c1cb4e', '#c7cb4a', '#cecb46', '#d4cb43', '#dacb3f', '#e0cb3b', '#e6cb37', '#ecca33', '#f3ca30', '#f9ca2c',
            ],
        },
        '500': {
            'summer': [
                '#ffc107', '#feb70d', '#fcad12', '#fba218', '#fa981e', '#f88e24', '#f7842a', '#f57a2f', '#f47035', '#f3653b', '#f15b40', '#f05146', '#ee474c', '#ed3d52', '#ec3258',
            ],
            'autumn': [
                '#e91e63', '#db276c', '#cc2f75', '#be387e', '#b04187', '#a14990', '#935299', '#845ba2', '#7664ac', '#686cb5', '#5975be', '#4b7ec7', '#3c86d0', '#2e8fd9', '#2098e2', '#11a0eb',
            ],
            'winter': [
                '#03a9f4', '#0babe9', '#14acdf', '#1caed4', '#25b0ca', '#2db1bf', '#36b3b4', '#3eb4aa', '#47b69f', '#4fb894', '#58b98a', '#60bb7f', '#69bc75', '#72be6a', '#7ac05f', '#82c155',
            ],
            'spring': [
                '#8bc34a', '#92c346', '#9ac342', '#a1c33d', '#a8c239', '#afc235', '#b6c231', '#bec22d', '#c5c229', '#ccc224', '#d3c220', '#dbc21c', '#e2c218', '#e9c114', '#f0c10f', '#f8c10b',
            ],
        },
        '600': {
            'summer': [
                '#ffb300', '#fdaa06', '#faa00c', '#f89612', '#f58d18', '#f3841e', '#f07a24', '#ee702a', '#ec6730', '#e95e36', '#e7543c', '#e44a42', '#e24148', '#df374e', '#dd2e54',
            ],
            'autumn': [
                '#d81b60', '#cb2368', '#bd2b71', '#b03379', '#a33b81', '#95438a', '#884b92', '#7b539a', '#6e5ba2', '#6063ab', '#536bb3', '#4673bb', '#387bc4', '#2b83cc', '#1e8bd4', '#1093dd',
            ],
            'winter': [
                '#039be5', '#0b9cdb', '#129ed1', '#1aa0c6', '#21a1bc', '#29a2b2', '#30a4a8', '#38a59e', '#40a794', '#47a889', '#4faa7f', '#56ab75', '#5ead6b', '#65ae61', '#6db056', '#74b24c',
            ],
            'spring': [
                '#7cb342', '#84b33e', '#8cb33a', '#95b336', '#9db332', '#a5b32d', '#adb329', '#b5b325', '#beb321', '#c6b31d', '#ceb319', '#d6b315', '#deb310', '#e6b30c', '#efb308', '#f7b304',
            ],
        },
        '700': {
            'summer': [
                '#ffa000', '#fb9806', '#f78f0b', '#f48611', '#f07e17', '#ec761c', '#e86d22', '#e46428', '#e05c2e', '#dd5433', '#d94b39', '#d5423f', '#d13a44', '#cd324a', '#ca2950',
            ],
            'autumn': [
                '#c2185b', '#b61f62', '#aa266a', '#9e2d71', '#923478', '#863b80', '#7a4287', '#6e498f', '#625096', '#56579d', '#4a5ea5', '#3e65ac', '#326cb4', '#2673bb', '#1a7ac2', '#0e81ca',
            ],
            'winter': [
                '#0288d1', '#0889c7', '#0f8bbe', '#158cb4', '#1c8eab', '#228fa1', '#289198', '#2f928e', '#359384', '#3b957b', '#429671', '#489868', '#4e995e', '#559b55', '#5b9c4b', '#629e42',
            ],
            'spring': [
                '#689f38', '#719f34', '#7b9f31', '#849f2e', '#8e9f2a', '#979f26', '#a19f23', '#aa9f20', '#b3a01c', '#bda018', '#c6a015', '#d0a012', '#d9a00e', '#e3a00a', '#eca007', '#f6a004',
            ],
        },
        '800': {
            'summer': [
                '#ff8f00', '#fa8705', '#f5800b', '#f07810', '#eb7016', '#e5691b', '#e06121', '#db5926', '#d6522c', '#d14a31', '#cc4236', '#c73a3c', '#c23341', '#bc2b47', '#b7234c',
            ],
            'autumn': [
                '#ad1457', '#a21a5d', '#982064', '#8d276a', '#822d70', '#783377', '#6d397d', '#623f84', '#58468a', '#4d4c90', '#425297', '#37589d', '#2d5ea4', '#2264aa', '#176bb0', '#0d71b7',
            ],
            'winter': [
                '#0277bd', '#0778b4', '#0c7aab', '#127ba2', '#177c9a', '#1c7d91', '#217e88', '#26807f', '#2c8176', '#31826d', '#368464', '#3b855b', '#408652', '#45874a', '#4b8841', '#508a38',
            ],
            'spring': [
                '#558b2f', '#608b2c', '#6a8b29', '#758c26', '#808c23', '#8a8c20', '#958c1d', '#9f8d1a', '#aa8d18', '#b58d15', '#bf8e12', '#ca8e0f', '#d48e0c', '#df8e09', '#ea8e06', '#f48f03',
            ],
        },
        '900': {
            'summer': [
                '#ff6f00', '#f86905', '#f0630a', '#e95d0f', '#e15714', '#da5119', '#d24b1e', '#cb4523', '#c33f28', '#bc382c', '#b53231', '#ad2c36', '#a6263b', '#9e2040', '#971a45',
            ],
            'autumn': [
                '#880e4f', '#801354', '#771759', '#6f1c5d', '#662062', '#5e2567', '#55296b', '#4d2e70', '#443375', '#3c377a', '#343c7e', '#2b4083', '#234588', '#1a498d', '#124e92', '#095296',
            ],
            'winter': [
                '#01579b', '#045893', '#07598b', '#0a5a84', '#0e5b7c', '#115d74', '#145e6c', '#175f64', '#1a605c', '#1d6155', '#20624d', '#236345', '#27653d', '#2a6635', '#2d672e', '#306826',
            ],
            'spring': [
                '#33691e', '#40691c', '#4d6a1a', '#596a18', '#666a16', '#736b15', '#806b13', '#8c6c11', '#996c0f', '#a66c0d', '#b26d0b', '#bf6d09', '#cc6e08', '#d96e06', '#e66e04', '#f26f02',
            ],
        },
        'A100': {
            'summer': [
                '#ffe57f', '#ffdf82', '#ffd884', '#ffd287', '#ffcc8a', '#ffc58d', '#ffbf90', '#ffb992', '#ffb295', '#ffac98', '#ffa69a', '#ffa09d', '#ff99a0', '#ff93a3', '#ff8da5',
            ],
            'autumn': [
                '#ff80ab', '#f786b0', '#ef8bb5', '#e790bb', '#df96c0', '#d79cc5', '#cfa1ca', '#c7a6d0', '#c0acd5', '#b8b2da', '#b0b7e0', '#a8bce5', '#a0c2ea', '#98c8ef', '#90cdf4', '#88d2fa',
            ],
            'winter': [
                '#80d8ff', '#85daf8', '#8addf1', '#8edfea', '#93e2e3', '#98e4dc', '#9ce7d5', '#a1e9ce', '#a6ecc8', '#abeec1', '#b0f0ba', '#b4f3b3', '#b9f5ac', '#bef8a5', '#c3fa9e', '#c7fd97',
            ],
            'spring': [
                '#ccff90', '#cffd8f', '#d2fc8e', '#d6fa8d', '#d9f88c', '#dcf78b', '#dff58a', '#e2f489', '#e6f288', '#e9f086', '#ecef85', '#efed84', '#f2ec83', '#f5ea82', '#f9e881', '#fce780',
            ],
        },
        'A200': {
            'summer': [
                '#ffd740', '#ffce44', '#ffc448', '#ffbb4c', '#ffb150', '#ffa854', '#ff9e58', '#ff955c', '#ff8c60', '#ff8265', '#ff7969', '#ff6f6d', '#ff6671', '#ff5c75', '#ff5379',
            ],
            'autumn': [
                '#ff4081', '#f34889', '#e75091', '#db5999', '#cf61a0', '#c369a8', '#b772b0', '#ab7ab8', '#a082c0', '#948ac8', '#8892d0', '#7c9bd8', '#70a3e0', '#64abe7', '#58b4ef', '#4cbcf7',
            ],
            'winter': [
                '#40c4ff', '#47c8f5', '#4ecbea', '#55cfe0', '#5cd3d6', '#64d6cb', '#6bdac1', '#72deb6', '#79e2ac', '#80e5a2', '#87e997', '#8eed8d', '#95f082', '#9df478', '#a4f86e', '#abfb63',
            ],
            'spring': [
                '#b2ff59', '#b7fc57', '#bcfa56', '#c0f854', '#c5f553', '#caf251', '#cff050', '#d4ee4e', '#d8eb4c', '#dde84b', '#e2e649', '#e7e448', '#ece146', '#f1de45', '#f5dc43', '#fada42',
            ],
        },
        'A400': {
            'summer': [
                '#ffc400', '#feb805', '#feac0b', '#fd9f10', '#fc9316', '#fc871b', '#fb7a21', '#fb6e26', '#fa622c', '#f95631', '#f94a36', '#f83d3c', '#f83141', '#f72547', '#f6184c',
            ],
            'autumn': [
                '#f50057', '#e60b62', '#d6166c', '#c72176', '#b82c81', '#a8378c', '#994296', '#8a4da0', '#7a58ab', '#6b63b6', '#5c6ec0', '#4d79cb', '#3d84d5', '#2e8fe0', '#1f9aea', '#0fa5f4',
            ],
            'winter': [
                '#00b0ff', '#07b5ef', '#0fbae0', '#16bfd0', '#1ec4c0', '#25c9b0', '#2ccea0', '#34d391', '#3bd881', '#42dc71', '#4ae162', '#51e652', '#58eb42', '#60f032', '#67f522', '#6ffa13',
            ],
            'spring': [
                '#76ff03', '#7ffb03', '#87f803', '#90f402', '#98f002', '#a1ed02', '#a9e902', '#b2e502', '#bbe202', '#c3de01', '#ccda01', '#d4d601', '#ddd301', '#e5cf01', '#eecb00', '#f6c800',
            ],
        },
        'A700': {
            'summer': [
                '#ffab00', '#fba106', '#f8980c', '#f48e12', '#f08418', '#ed7b1f', '#e97125', '#e6682b', '#e25e31', '#de5437', '#db4b3d', '#d74143', '#d4384a', '#d02e50', '#cc2456',
            ],
            'autumn': [
                '#c51162', '#b9196a', '#ac2173', '#a0297c', '#943184', '#87398c', '#7b4195', '#6f499e', '#6251a6', '#5659ae', '#4a61b7', '#3e69c0', '#3171c8', '#2579d0', '#1981d9', '#0c89e2',
            ],
            'winter': [
                '#0091ea', '#0696dd', '#0c9bd0', '#139fc2', '#19a4b5', '#1fa9a8', '#26ae9b', '#2cb28e', '#32b780', '#38bc73', '#3ec166', '#45c559', '#4bca4c', '#51cf3f', '#58d331', '#5ed824',
            ],
            'spring': [
                '#64dd17', '#6eda16', '#77d714', '#81d413', '#8bd011', '#94cd10', '#9eca0e', '#a8c70d', '#b2c40c', '#bbc10a', '#c5be09', '#cfbb07', '#d8b806', '#e2b404', '#ecb103', '#f5ae01',
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



def common_assert(case, response,status_code, code, data):

    case.assertEqual(status_code, response.status_code)
    case.assertEqual(code, response.json().get("code"))
    case.assertIn(data, response.json().get("data"))

def common_assert01(case, response,status_code, code,):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(code, response.json().get("code"))

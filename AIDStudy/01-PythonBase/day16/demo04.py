# 分苹果
def div_apple(apple_count):
    person_count = int(input('请输入人数:'))  # ValueError #KeyboardInterrupt
    res = apple_count / person_count  # ZeroDivisionError
    print('每个人分到了%s个苹果' % res)


if __name__ == '__main__':
    try:
        # 可能出现异常的语句
        div_apple(10)
    except ValueError:
        # 处理异常的语句
        print('人数必须为整数')
    except ZeroDivisionError:
        print('人数不能为零')
    except KeyboardInterrupt:
        print('\n用户中断输入')
    except Exception:
        print('未知错误')
    else:
        # 没有发生异常执行的语句
        print('没有异常发生')
    finally:
        # 不管有没有发生异常一定要执行的语句
        print('程序结束')

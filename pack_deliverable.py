# -*- coding: utf-8 -*-
"""交付包打包脚本：白名单模式，只收结果产物 + 使用说明。

交付内容（结果产物 + 怎么用）：
  auto_change_phone.py  自动化主脚本（配置已内置，单文件自包含）
  README.md             使用说明

用法：python pack_deliverable.py （在 deliverables/ 目录下运行）
输出：deliverables/meituan_login_auto_交付包_2026-11-13.zip
"""
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
# 输出锚定 deliverables/（脚本父目录），与 CWD 无关
OUT = os.path.join(os.path.dirname(ROOT),
                   "meituan_login_auto_交付包_2026-11-13.zip")

# 白名单：交付包只含以下文件（其余开发/验证文件一律不进包）
# R36 起 ddddocr OCR 内嵌进主脚本，交付回归单文件
INCLUDE = {
    "auto_change_phone.py",
    "README.md",
}


def main():
    count = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in sorted(INCLUDE):
            full = os.path.join(ROOT, fn)
            assert os.path.isfile(full), "缺少交付文件：%s" % fn
            z.write(full, os.path.join(os.path.basename(ROOT), fn))
            count += 1
    # 完整性校验 + 清单输出
    z2 = zipfile.ZipFile(OUT)
    bad = z2.testzip()
    print("integrity:", "OK" if bad is None else "BAD: %s" % bad)
    print("size: %.2f MB" % (os.path.getsize(OUT) / 1048576.0))
    for name in sorted(z2.namelist()):
        print(" ", name)


if __name__ == "__main__":
    main()

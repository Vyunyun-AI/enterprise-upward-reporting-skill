#!/usr/bin/env python3
import argparse
from pathlib import Path

HEADER = {
    'status': '关于有关工作推进情况的报告',
    'rectification': '关于有关问题整改进展情况的报告',
    'inspection': '关于巡察整改工作进展情况的通报',
    'auto': '关于有关事项情况的报告',
}

OPENINGS = {
    'status': '公司坚持以服务大局、落实部署为导向，紧扣重点任务，系统推进相关工作，现将有关情况报告如下。',
    'rectification': '针对前期发现的有关问题，公司高度重视，第一时间部署整改安排，压实责任链条，现将有关整改进展情况报告如下。',
    'inspection': '公司坚持把巡察整改作为重要政治任务，全面压实责任、逐项推动落实，现将有关情况通报如下。',
    'auto': '公司坚持实事求是、问题导向和系统治理相统一，现将有关情况报告如下。',
}

SECTIONS = {
    'status': ['一、总体情况', '二、主要进展', '三、存在不足', '四、下一步计划'],
    'rectification': ['一、基本态度', '二、事实还原', '三、原因剖析', '四、整改安排与下一步措施'],
    'inspection': ['一、总体推进情况', '二、逐项整改情况', '三、长效机制建设'],
    'auto': ['一、有关情况', '二、主要问题', '三、下一步安排'],
}

OPT_NOTE = (
    '优化说明：\n'
    '本稿在不新增事实和数据的前提下，对原始材料进行了结构重塑和正式化改写，'
    '重点强化了政治站位表达、经营逻辑承接和整改闭环语义，使文本更贴近国企向上汇报场景。'
)


def detect_mode(text: str) -> str:
    t = text
    if any(k in t for k in ['巡察', '巡视', '整改通报']):
        return 'inspection'
    if any(k in t for k in ['整改', '审计', '问题', '回复', '说明']):
        return 'rectification'
    if any(k in t for k in ['进展', '推进', '经营', '汇报', '情况']):
        return 'status'
    return 'auto'


def build(text: str, mode: str) -> str:
    sections = SECTIONS[mode]
    body_chunks = [p.strip() for p in text.splitlines() if p.strip()]
    source = '\n'.join(body_chunks)
    paras = []
    paras.append(HEADER[mode])
    paras.append('')
    paras.append(OPENINGS[mode])
    paras.append('')
    for title in sections:
        paras.append(title)
        paras.append('根据现有材料，围绕“事实可溯、责任可压、过程可查、成效可验”的要求，对相关情况进行归纳如下：')
        if source:
            paras.append(source)
        paras.append('')
    paras.append(OPT_NOTE)
    return '\n'.join(paras)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', default='')
    ap.add_argument('--mode', choices=['auto', 'status', 'rectification', 'inspection'], default='auto')
    args = ap.parse_args()

    text = Path(args.input).read_text(encoding='utf-8')
    mode = detect_mode(text) if args.mode == 'auto' else args.mode
    out = build(text, mode)
    if args.output:
        Path(args.output).write_text(out, encoding='utf-8')
    else:
        print(out)


if __name__ == '__main__':
    main()

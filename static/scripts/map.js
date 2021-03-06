define('map', function() {
  var cityMap = {
    'Guangzhou': '广州',
    'Beijing': '北京',
    'Shanghai': '上海',
    'Chengdu': '成都',
    'Shenyang': '沈阳'
  };

  var levelMap = {
    '-1': {
      'text': '未知',
      'description': '无',
      'suggestion': '无'
    },
    '1': {
      'text': '一级（优）',
      'description': '空气质量令人满意，基本无空气污染',
      'suggestion': '各类人群可正常活动'
    },
    '2': {
      'text': '二级（良）',
      'description': '空气质量可接受，但某些污染物可能对极少数异常敏感人群健康有较弱影响',
      'suggestion': '极少数异常敏感人群应减少户外活动'
    },
    '3': {
      'text': '三级（轻度污染）',
      'description': '易感人群症状有轻度加剧，健康人群出现刺激症状',
      'suggestion': '儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼'
    },
    '4': {
      'text': '四级（中度污染）',
      'description': '进一步加剧易感人群症状，可能对健康人群心脏、呼吸系统有影响',
      'suggestion': '儿童、老年人及心脏病、呼吸系统疾病患者避免长时间、高强度的户外锻炼，一般人群适量减少户外运动'
    },
    '5': {
      'text': '五级（重度污染）',
      'description': '心脏病和肺病患者症状显著加剧，运动耐受力降低，健康人群普遍出现症状',
      'suggestion': '儿童、老年人及心脏病、肺病患者应停留在室内，停止户外运动，一般人群减少户外运动'
    },
    '6': {
      'text': '六级（严重污染）',
      'description': '健康人群运动耐受力降低，有明显强烈症状，提前出现某些疾病',
      'suggestion': '儿童、老年人和病人应停留在室内，避免体力消耗，一般人群避免户外活动'
    }
  };

  return {
    'city': cityMap,
    'level': levelMap
  };
});

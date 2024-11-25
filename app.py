from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# 感情分析用モデルのロード
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_text():
    # ファイルを受け取る
    file = request.files['file']
    text = file.read().decode('utf-8')

    # 感情分析
    sentiments = sentiment_analyzer(text[:512])  # 最初の512文字を制限

    # 簡単な文章スタイル分析
    sentences = text.split('.')
    avg_sentence_length = sum(len(s) for s in sentences) / len(sentences) if sentences else 0
    word_count = len(text.split())
    unique_words = len(set(text.split()))
    lexical_diversity = unique_words / word_count if word_count > 0 else 0

    # 結果を返す
    result = {
        "sentiments": sentiments,
        "style_analysis": {
            "average_sentence_length": avg_sentence_length,
            "word_count": word_count,
            "lexical_diversity": lexical_diversity
        }
    }
    return jsonify(result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

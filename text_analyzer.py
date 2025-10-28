import re
from collections import Counter

class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.words = self._extract_words()
        
    def _extract_words(self):
        """Extract words from text, removing punctuation"""
        return re.findall(r'\b[a-zA-Z]+\b', self.text.lower())
    
    def word_count(self):
        """Count total words in text"""
        return len(self.words)
    
    def character_count(self, include_spaces=True):
        """Count characters in text"""
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(" ", ""))
    
    def sentence_count(self):
        """Count sentences in text"""
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])
    
    def average_word_length(self):
        """Calculate average word length"""
        if not self.words:
            return 0
        return round(sum(len(word) for word in self.words) / len(self.words), 2)
    
    def most_common_words(self, n=5):
        """Get the n most common words"""
        # Filter out common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'was', 'are', 'were'}
        filtered_words = [word for word in self.words if word not in stop_words]
        return Counter(filtered_words).most_common(n)
    
    def sentiment_score(self):
        """Simple sentiment analysis based on positive/negative word lists"""
        positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 
            'awesome', 'love', 'happy', 'joy', 'beautiful', 'perfect', 'best',
            'brilliant', 'positive', 'success', 'successful', 'delightful'
        }
        negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'poor', 'worst', 'hate',
            'sad', 'angry', 'negative', 'failure', 'failed', 'disappointing',
            'disappointed', 'ugly', 'wrong', 'difficult', 'problem'
        }
        
        positive_count = sum(1 for word in self.words if word in positive_words)
        negative_count = sum(1 for word in self.words if word in negative_words)
        
        total = positive_count + negative_count
        if total == 0:
            return "Neutral", 0.0
        
        sentiment_ratio = (positive_count - negative_count) / len(self.words)
        
        if sentiment_ratio > 0.02:
            return "Positive", round(sentiment_ratio, 3)
        elif sentiment_ratio < -0.02:
            return "Negative", round(sentiment_ratio, 3)
        else:
            return "Neutral", round(sentiment_ratio, 3)
    
    def readability_score(self):
        """Calculate a simple readability score (Flesch Reading Ease approximation)"""
        words = self.word_count()
        sentences = self.sentence_count()
        syllables = sum(self._count_syllables(word) for word in self.words)
        
        if sentences == 0 or words == 0:
            return 0
        
        # Simplified Flesch Reading Ease formula
        score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
        return round(max(0, min(100, score)), 2)
    
    def _count_syllables(self, word):
        """Estimate syllable count in a word"""
        word = word.lower()
        count = 0
        vowels = 'aeiouy'
        previous_was_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                count += 1
            previous_was_vowel = is_vowel
        
        # Adjust for silent 'e'
        if word.endswith('e'):
            count -= 1
        
        # Ensure at least one syllable
        return max(1, count)
    
    def analyze(self):
        """Perform complete text analysis"""
        sentiment, sentiment_score = self.sentiment_score()
        
        analysis = {
            "word_count": self.word_count(),
            "character_count": self.character_count(),
            "character_count_no_spaces": self.character_count(include_spaces=False),
            "sentence_count": self.sentence_count(),
            "average_word_length": self.average_word_length(),
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
            "readability_score": self.readability_score(),
            "most_common_words": self.most_common_words()
        }
        
        return analysis
    
    def __str__(self):
        """Return formatted analysis results"""
        analysis = self.analyze()
        
        result = f"""📝 TEXT ANALYSIS RESULTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Basic Metrics:
   • Words: {analysis['word_count']}
   • Characters: {analysis['character_count']} (with spaces) | {analysis['character_count_no_spaces']} (without spaces)
   • Sentences: {analysis['sentence_count']}
   • Avg Word Length: {analysis['average_word_length']} characters

💭 Sentiment Analysis:
   • Overall Sentiment: {analysis['sentiment']}
   • Sentiment Score: {analysis['sentiment_score']}

📖 Readability:
   • Readability Score: {analysis['readability_score']}/100
   • Level: {self._get_readability_level(analysis['readability_score'])}

🔤 Most Common Words:
"""
        for word, count in analysis['most_common_words']:
            result += f"   • '{word}': {count} times\n"
        
        return result
    
    def _get_readability_level(self, score):
        """Convert readability score to difficulty level"""
        if score >= 90:
            return "Very Easy (5th grade)"
        elif score >= 80:
            return "Easy (6th grade)"
        elif score >= 70:
            return "Fairly Easy (7th grade)"
        elif score >= 60:
            return "Standard (8th-9th grade)"
        elif score >= 50:
            return "Fairly Difficult (10th-12th grade)"
        elif score >= 30:
            return "Difficult (College)"
        else:
            return "Very Difficult (College graduate)"


if __name__ == "__main__":
    sample_text = input("Enter text to analyze: ")
    analyzer = TextAnalyzer(sample_text)
    print(analyzer)


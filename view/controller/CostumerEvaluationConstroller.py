# Der CostumerEvaluationController behinhaltet Funktionen die dazu dienen Kundenbewertungen zu schreiben,zu finden und auszugeben.
from models.classCostumerEvaluation import CostumerEvaluation

review = CostumerEvaluation("P100","Hallo","Hallo")

class CostumerEvaluationController:
    CostumerEvaluationList=[]
    CostumerEvaluationList_Flask = []
    ReviewsToDeleteInFlask = []

#Die create_new_reviews Funtion dient dazu das Kunden eine Bewertung zu einem bestimmten Produkt schreiben können.
    def create_new_reviews(self,RID,head,reviews):
        costumer_reviews=CostumerEvaluation(RID=RID,head=head,reviews=reviews)
        self.CostumerEvaluationList.append(costumer_reviews)

#Diese Funktion ist auch extra für Flask definiert und gibt alle Review für ein Product aus.
#Die CostumerEvaluationList_Flask wird am ende geleert, weil sonst nach der Abfrage die Reviews stehen geblieben sind.
#Dadurch wurde bei erneuter Abfrage eines anderen Produktes auch die Reviews der ersten Abfrage ausgegeben.
#Deshalb werden die Reviews in einer anderen Liste zwischengespreicher, welche dann in der View aufgerufen wird.(ReviewsToDeleteInFlask)
#Somit werden nur die Reviews aufgerufen die jetzt angerfagt wurden.
    def get_all_reviews(self,RID):
        self.find_reviews_Flask(RID)
        for review in self.CostumerEvaluationList_Flask:
            if review.RID == RID:
                self.ReviewsToDeleteInFlask.append(review)
        self.CostumerEvaluationList_Flask.clear()

#Die find_reviews dient dazu eien bestimmte Kundenbewertung anhand der RID (Review ID) zu finden und zurückzugeben.
    def find_reviews(self,RID):
        for review in self.CostumerEvaluationList:
            if review.RID == RID:
                return review

#Funktion arbeitet der get_all_reviews zu. Sie speichert die gefragten Elemente in der CostumerEvaluationList_Flask.
    def find_reviews_Flask(self,RID):
        for review in self.CostumerEvaluationList:
            if review.RID == RID:
                self.CostumerEvaluationList_Flask.append(review)

    review1 = CostumerEvaluation("P1", "Nice Shoe", "good quality")
    review2 = CostumerEvaluation("P2", "good", "nice quality but really expensive")
    review3 = CostumerEvaluation("P3", "Bad", "way to expensive for this quality")
    review4 = CostumerEvaluation("P4", "Nice", "multifunctional use")
    review5 = CostumerEvaluation("P5", "ok", "good to makes sport but not more")
    CostumerEvaluationList.append(review1)
    CostumerEvaluationList.append(review2)
    CostumerEvaluationList.append(review3)
    CostumerEvaluationList.append(review4)
    CostumerEvaluationList.append(review5)





